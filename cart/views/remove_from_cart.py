from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from cart.models import Cart, CartItems


def remove_from_cart(request):
    # Получаем id блюда из POST-запроса
    dish_id = request.POST.get('dish_id')

    # Если пользователь аутентифицирован
    if request.user.is_authenticated:
        # Получаем корзину пользователя
        cart = Cart.objects.filter(user=request.user).first()
    else:
        # Получаем сессионный ключ пользователя
        session_key = request.session.session_key

        # Если сессионного ключа нет, сохраняем его
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        # Получаем корзину анонимного пользователя
        cart = Cart.objects.filter(session_key=session_key).first()

    # Если корзина пользователя существует
    if cart:
        # Получаем элемент корзины для данного блюда в корзине пользователя
        cart_item = get_object_or_404(CartItems, cart=cart, dish_id=dish_id)

        # Если количество выбранного блюда больше 1, уменьшаем его на 1
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            quantity_in_cart = cart_item.quantity
            cart_item.save()
        # Иначе удаляем элемент корзины
        else:
            cart_item.delete()
            quantity_in_cart = 0

        # Получаем промежуточную стоимость выбранного блюда (если элемент корзины существует) или устанавливаем равной 0
        subtotal = cart_item.subtotal() if cart_item else 0
        # Получаем общую стоимость всех блюд в корзине (если корзина существует) или устанавливаем равной 0
        total = cart.total_cost() if cart else 0
        total_with_service = cart.total_cost_with_service()

        # Возвращаем JSON-ответ с информацией о удалении блюда из корзины
        return JsonResponse(
            {
                'success': True,
                'subtotal': subtotal,
                'total': total,
                'total_with_service': total_with_service,
                'quantity': quantity_in_cart,
            }
        )
