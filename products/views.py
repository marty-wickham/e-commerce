from django.shortcuts import render
from .models import Product

# Create your views here.
def get_products(request):
    """
    A view to retrieve and display all products from the database.
    """
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
