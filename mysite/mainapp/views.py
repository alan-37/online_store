from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'mainapp/shop.html', context)

def about(request):
    return render(request, 'mainapp/about.html')

def faq(request):
    return render(request, 'mainapp/faq.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def reviews(request):
    return render(request, 'mainapp/reviews.html')

def product(request, product_id):
    product_ids = Product.objects.get(id=product_id)
    product_all = Product.objects.all()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    context = {
        'product': product_ids,
        'product_all': product_all
    }
    return render(request, 'mainapp/product.html', context)