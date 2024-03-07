from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from cart.models import Cart, CartItems
from main.models import Dish


def add_to_cart(request):
    # Получаем id блюда из POST-запроса
    dish_id = request.POST.get('dish_id')
    # Получаем объект блюда по его id или возвращаем ошибку 404, если блюдо не найдено
    dish = get_object_or_404(Dish, pk=dish_id)
    # Получаем пользователя, отправившего запрос
    user = request.user

    # Если пользователь аутентифицирован
    if request.user.is_authenticated:
        # Получаем или создаем корзину пользователя
        cart, created = Cart.objects.get_or_create(user=user)
    else:
        # Если пользователь не аутентифицирован, используем его сессионный ключ для создания или получения корзины
        session_key = request.session.session_key

        # Если сессионного ключа нет, сохраняем его
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        # Получаем или создаем корзину для анонимного пользователя
        cart, created = Cart.objects.get_or_create(
            session_key=session_key, user_id=None
        )

    # Получаем или создаем элемент корзины для данного блюда в корзине пользователя
    cart_item, item_created = CartItems.objects.get_or_create(cart=cart, dish=dish)

    # Увеличиваем количество выбранного блюда на 1 или устанавливаем его равным 1, если элемент корзины был только что создан
    if item_created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1

    # Получаем количество выбранного блюда в корзине
    quantity_in_cart = cart_item.quantity
    cart_item.save()

    # Получаем промежуточную стоимость выбранного блюда
    subtotal = cart_item.subtotal()
    # Получаем общую стоимость всех блюд в корзине
    total = cart.total_cost()
    total_with_service = cart.total_cost_with_service()

    # Возвращаем JSON-ответ с информацией о добавленном блюде в корзину
    return JsonResponse(
        {
            'success': True,
            'subtotal': subtotal,
            'total': total,
            'total_with_service': total_with_service,
            'quantity': quantity_in_cart,
        }
    )
