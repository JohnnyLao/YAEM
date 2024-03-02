from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from cart.models import Cart, CartItems


def remove_from_cart(request):
    dish_id = request.POST.get('dish_id')

    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).first()

        if user_cart:
            cart_item = get_object_or_404(CartItems, cart=user_cart, dish_id=dish_id)

            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

            subtotal = cart_item.subtotal()
            total = user_cart.total_cost()

            return JsonResponse({'success': True, 'subtotal': subtotal, 'total': total})
