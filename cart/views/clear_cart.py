from django.shortcuts import redirect

from cart.models import Cart, CartItems


def cart_remove(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).first()
        if user_cart:
            user_cart.cart_items.all().delete()
    else:
        session_key = request.session.session_key
        if session_key:
            user_cart = Cart.objects.filter(session_key=session_key).first()
            if user_cart:
                user_cart.cart_items.all().delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))
