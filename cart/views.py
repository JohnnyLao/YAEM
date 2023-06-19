from django.http import JsonResponse
from django.shortcuts import render, redirect
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
        if product_id and product_id in cart:
            cart[product_id] += int(quantity)
        elif product_id:
            cart[product_id] = int(quantity)

        request.session.modified = True

        return JsonResponse({'success': True})


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []
        sub_total_price = 0
        total_price = 0

        for product_id, quantity in cart.items():
            try:
                product = Dish.objects.get(id=product_id)
                cart_item = {
                    'product': product,
                    'quantity': quantity,
                    'sub_total': product.actual_price * quantity,
                }
                cart_items.append(cart_item)
                sub_total_price += cart_item['sub_total']
            except Dish.DoesNotExist:
                pass

        total_price = sub_total_price  # Вычисление общей суммы

        context = {
            'cart_items': cart_items,
            'sub_total_price': sub_total_price,
            'total_price': total_price,
        }

        return render(request, 'cart/cart.html', context=context)

    def post(self, request):
        product_id = request.POST.get('product_id')

        if product_id:
            cart = request.session.get('cart', {})
            if product_id in cart:

                cart[product_id] -= 1
                if cart[product_id] <= 0:
                    del cart[product_id]
                request.session['cart'] = cart
                return JsonResponse({'success': True})

        return JsonResponse({'success': False})



