from django.shortcuts import render
from products.models import Product

# Create your views here.
def search(request):
    # This will get whatever 'q' is returned from the form, so we'll give the form a name of 'q'.
    products = Products.objects.filter(name__icontains=request.get['q'])
    return render(request, "products.html", {"products": products})
