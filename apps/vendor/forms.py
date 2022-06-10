from pyexpat import model
from django.forms import ModelForm
from django import forms
from .models import Info
from apps.product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

class VendorForm(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = Info
        fields = ['first_name', 'last_name', 'email', 'phone']
