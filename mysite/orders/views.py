from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .forms import OrderCreateForm
from .models import ProductInBasket, ProductInOrder, Order
from users.models import CustomUser


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={'nmb': nmb})
    if not created:
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    product_total_nmb = products_in_basket.count()
    return_dict["product_total_nmb"] = product_total_nmb
    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["max"] = item.product.quantity
        product_dict["total_price"] = item.total_price
        if item.nmb < item.product.quantity:
            product_dict["nmb"] = item.nmb
        else:
            product_dict["nmb"] = item.product.quantity

        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)


def checkout(request):
    user_all = CustomUser.objects.all()
    form = OrderCreateForm(request.POST or None)

    session_key = request.session.session_key

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, order__isnull=True)
    context = {
        "user": request.user,
        "users": user_all,
        "form": form,
        "products_in_basket":products_in_basket,
    }
    user = CustomUser.objects.all()
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            email = data.get('email')
            name = data.get('name', None)
            address = data.get('address')
            phone = data.get('phone')
            user, created = CustomUser.objects.get_or_create(email=email,
                                                          address=address,
                                                          phone=phone, defaults={'first_name':name, })
            order = Order.objects.create(user=user,customer_name=name,
                                          customer_email=email,
                                          customer_address=address,
                                          customer_phone=phone)
            for name, value in data.items():
                if name.startswith('product_'):
                    id = name.split('product_')[1]
                    product = ProductInBasket.objects.get(id=id)
                    product.order = order
                    product.nmb = value
                    product.save(force_update=True)
                    ProductInOrder.objects.create(product=product.product, nmb=product.nmb,
                                                   total_price=product.total_price,
                                                   created=product.created,
                                                   order=order)
                    product.delete()
            return render(request, 'orders/order_info.html', context)

        else:
            print('no')

    return render(request, 'orders/checkout.html', context)


def delete_cart(request, id):
    product_id = request.GET.get('id')
    product = ProductInBasket.objects.get(id=id)
    product.delete()
    return redirect(reverse('checkout'))


def order_info(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, order__isnull=True)
    order_id = Order.objects.all()
    context = {
        "order_id": order_id,
        "products_in_basket": products_in_basket,
    }
    return render(request, 'orders/order_info.html', context)