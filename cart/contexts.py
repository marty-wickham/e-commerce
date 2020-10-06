from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensure that the cart contents are available when rendering every page.
    """
    # Requests the existing cart if there is one, or a blank dictionary if there's not.
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        prodcut = get_object_or_404(Product, pk=id)
        total += quantity * prodcut.price
        product_count =+ quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': prodcut})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
