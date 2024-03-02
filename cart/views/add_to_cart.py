from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from cart.models import Cart, CartItems
from main.models import Dish


def add_to_cart(request):
    dish_id = request.POST.get('dish_id')
    dish = get_object_or_404(Dish, pk=dish_id)
    user = request.user

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItems.objects.get_or_create(cart=cart, dish=dish)

        if item_created:
            cart_item.quantity = 1
        else:
            cart_item.quantity += 1
        cart_item.save()

        subtotal = cart_item.subtotal()
        total = cart.total_cost()

        return JsonResponse({'success': True, 'subtotal': subtotal, 'total': total})
