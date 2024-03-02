from django.shortcuts import redirect

from cart.models import CartItems, Cart


def cart_remove(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).first()
        if user_cart:
            user_cart.cart_items.all().delete()
    return redirect(request.META['HTTP_REFERER'])
