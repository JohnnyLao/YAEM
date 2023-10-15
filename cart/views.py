import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from main.models import Dish


class ViewCartPage(View):
    def get(self, request):
        cart = request.session.get("cart", {})
        cart_items = []
        sub_total_price = 0
        total_price = 0

        for product_id, quantity in cart.items():
            product = get_object_or_404(Dish, id=product_id)
            cart_item = {
                "product": product,
                "quantity": quantity,
                "sub_total": product.actual_price * quantity,
            }
            cart_items.append(cart_item)
            sub_total_price += cart_item["sub_total"]
        total_price = sub_total_price
        context = {
            "cart_items": cart_items,
            "sub_total_price": sub_total_price,
            "total_price": total_price,
            "is_empty": len(cart_items) == 0,
        }
        return render(request, "cart/cart.html", context=context)


class AddToCart(View):
    def post(self, request, product_id):
        product = get_object_or_404(Dish, id=product_id)
        quantity = int(request.POST.get("add_quantity", 1))
        if "cart" not in request.session:
            request.session["cart"] = {}
        cart = request.session["cart"]
        key = str(product_id)
        if key in cart:
            cart[key] += quantity
        else:
            cart[key] = quantity
        request.session.modified = True
        total_price = 0
        for product_id, quantity in cart.items():
            product = get_object_or_404(Dish, id=product_id)
            sub_total = product.actual_price * quantity
            total_price += sub_total
        html = """<span  data-aos="fade-up" class="fs-3 my-0 py-0"> 
                        <i class="fas fa-cart-shopping my-0 py-0"></i>"""
        formatted_total_price = f'{html} {total_price:,} ₸</span>'.replace(',', ' ')
        return HttpResponse(formatted_total_price)


class RemoveFromCart(View):
    def post(self, request, product_id):
        product = get_object_or_404(Dish, id=product_id)
        quantity = int(request.POST.get("remove_quantity", 1))
        cart = request.session.get("cart", {})
        key = str(product_id)
        cart[key] = max(cart.get(key, 0) - quantity, 0)
        if cart[key] == 0:
            del cart[key]
        request.session.modified = True
        total_price = 0
        for product_id, quantity in cart.items():
            product = get_object_or_404(Dish, id=product_id)
            sub_total = product.actual_price * quantity
            total_price += sub_total
        html = """<span  data-aos="fade-up" class="fs-3 my-0 py-0" style="color: #fd7014; background: rgba(33, 37, 41, 0.5)"> 
                                <i class="fas fa-cart-shopping my-0 py-0"></i>"""
        formatted_total_price = f'{html} {total_price:,} ₸</span>'.replace(',', ' ')
        if total_price == 0:
            formatted_total_price = f''
            return HttpResponse(formatted_total_price)
        return HttpResponse(formatted_total_price)


class RemoveFromCartOnCartPage(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        cart = request.session['cart']
        if product_id in cart:
            if cart[product_id] == 1:
                del cart[product_id]
            else:
                cart[product_id] -= 1
            request.session.modified = True
        return redirect(reverse("cart:cart_page"))


class CartClearView(View):
    def post(self, request):
        request.session["cart"] = {}  # Очистка корзины
        return redirect(reverse("cart:cart_page"))
