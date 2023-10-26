from main.models import Client, Dish
from random import randint


def data_counter_site(request):
    total_dishes = Dish.objects.count()
    total_clients = Client.objects.count()
    total_orders = total_clients * randint(20, 50)

    return {
        "total_dishes": total_dishes,
        "total_clients": total_clients,
        "total_orders": total_orders,
    }

# def cart_items_count(request):
#     cart = request.session.get('cart', {})
#     print(cart)
#     return {'counter_cart_items': len(cart)}
