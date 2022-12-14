from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from orders.models import Order, ProductInOrder


def regedit(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/regedit.html', {'form': form})

def profile(request):
    user_all = CustomUser.objects.all()
    customer = CustomUser.objects.get(email=request.user.email)
    order = Order.objects.filter(user=customer)
    context = {
        "user": request.user,
        "users": user_all,
        "order": order
    }
    return render(request, 'users/profile.html', context)

