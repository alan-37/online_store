from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control input-text'}))
    first_name = forms.CharField(label='Имя', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control input-text'}))
    last_name = forms.CharField(label='Фамилия', max_length=35, widget=forms.TextInput(attrs={'class': 'form-control input-text'}))
    address = forms.CharField(label='Адрес', max_length=225, widget=forms.TextInput(attrs={'class': 'form-control input-text'}))
    phone = forms.CharField(label='Телефон', max_length=12, min_length=11,widget=forms.TextInput(attrs={'class': 'form-control input-text'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control input-text'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control input-text'}))
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name', 'phone', 'address')