from django.contrib import messages
from django.shortcuts import redirect

from cart.models import Cart, CartItems


def cart_remove(request):
    # Если пользователь аутентифицирован
    if request.user.is_authenticated:
        # Получаем корзину пользователя
        user_cart = Cart.objects.filter(user=request.user).first()
        # Если у пользователя есть корзина
        if user_cart:
            # Удаляем все элементы корзины
            user_cart.cart_items.all().delete()
    else:
        # Получаем сессионный ключ пользователя
        session_key = request.session.session_key
        # Если сессионный ключ существует
        if session_key:
            # Получаем корзину анонимного пользователя
            user_cart = Cart.objects.filter(session_key=session_key).first()
            # Если у пользователя есть корзина
            if user_cart:
                # Удаляем все элементы корзины
                user_cart.cart_items.all().delete()

    messages.warning(request, message='Корзина очищена.')
    # Перенаправляем пользователя на предыдущую страницу
    return redirect(request.META.get('HTTP_REFERER'))
