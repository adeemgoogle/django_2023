from django.shortcuts import render

from .models import ProductCategory, Product
# Create your views here.

def index(request):
    context = {
        'title': 'storeApp',
        'username': 'Adema',
        'is_promotion': True,
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'StoreProducts/index.html')



def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'StoreProducts/products.html', context)