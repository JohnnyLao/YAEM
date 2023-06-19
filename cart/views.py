from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from main.models import Dish


class AddToCartView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        if not product_id or not product_id.isdigit():
            return JsonResponse({'success': False, 'error': 'Invalid product_id'})

        if not quantity or not quantity.isdigit():
            return JsonResponse({'success': False, 'error': 'Invalid quantity'})

        # Проверка наличия корзины в сессии
        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session['cart']

        # Добавление товара в корзину
        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)

        request.session.modified = True

        return JsonResponse({'success': True})


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})

        # Получение информации о товарах в корзине
        cart_items = []
        for product_id, quantity in cart.items():
            # Получение информации о товаре по его идентификатору
            try:
                product = Dish.objects.get(id=product_id)
                cart_item = {
                    'product': product,
                    'quantity': quantity
                }
                cart_items.append(cart_item)
            except Dish.DoesNotExist:
                pass

        return render(request, 'cart/cart.html', {'cart_items': cart_items})
