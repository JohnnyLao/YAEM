from django import template

from cart.models import Cart, CartItems
from main.models import Dish

register = template.Library()


@register.simple_tag()
def user_cart(request, establishment_url):
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).first()
        if user_cart:
            establishment_dishes_ids = Dish.objects.filter(
                food_type__category__client__url_name=establishment_url
            ).values_list('id', flat=True)
            CartItems.objects.filter(cart=user_cart).exclude(
                dish_id__in=establishment_dishes_ids
            ).delete()
        return user_cart
    else:
        session_key = request.session.session_key

        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        user_cart, _ = Cart.objects.get_or_create(session_key=session_key)
        establishment_dishes_ids = Dish.objects.filter(
            client__url_name=establishment_url
        ).values_list('id', flat=True)
        CartItems.objects.filter(cart=user_cart).exclude(
            dish_id__in=establishment_dishes_ids
        ).delete()

        return user_cart


@register.filter()
def get_item(dictionary, key):
    return dictionary.get(key, '')
