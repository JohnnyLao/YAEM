from random import randint

from banquets.models import BanquetCard
from main.models import City, Client, Dish


def data_counter_site(request):
    total_dishes = Dish.objects.count()
    total_clients = Client.objects.count()
    total_orders = total_clients * randint(9, 15)

    total_banquets = BanquetCard.objects.count()
    total_cities = City.objects.count()

    return {
        "total_dishes": total_dishes,
        "total_clients": total_clients,
        "total_orders": total_orders,
        "total_banquets": total_banquets,
        "total_cities": total_cities,
    }


# def cart_items_count(request):
#     cart = request.session.get('cart', {})
#     print(cart)
#     return {'counter_cart_items': len(cart)}
