from django.shortcuts import render

from apps.product.models import Product

# Create your views here.
def frontpage(request):
    newest_products = Product.objects.all()[0:5]
    all_products = Product.objects.all()
    return render(request, 'core/frontpage.html', {'newest_products': newest_products, 'all_products': all_products})

def contact(request):
    return render(request, 'core/contact.html')