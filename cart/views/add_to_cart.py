from cart.models import Cart, CartItems
from main.models import Dish
from django.shortcuts import get_object_or_404, redirect


def add_to_cart(request, dish_id):
    dish = Dish.objects.filter(pk=dish_id).first()
    user = request.user

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItems.objects.get_or_create(cart=cart, dish=dish)

        if item_created:
            cart_item.quantity = 1
        else:
            cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META['HTTP_REFERER'])
