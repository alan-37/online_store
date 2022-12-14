from django import forms
from .models import Order

class OrderCreateForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True, max_length=11)
    address = forms.CharField(required=True)
    email = forms.CharField(required=True)