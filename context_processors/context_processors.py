from datetime import datetime
from random import randint

from django.core.cache import cache

from banquets.models import BanquetCard
from cart.models import Cart
from main.models import City, Client, Dish


def data_counter_site(request):
    cache_data = cache.get('site_counters')
    if cache_data:
        return cache_data

    total_dishes = Dish.objects.count()
    total_clients = Client.objects.count()
    total_online = generate_random_number()

    total_banquets = BanquetCard.objects.count()
    total_cities = City.objects.count()

    site_counters = {
        "total_dishes": total_dishes,
        "total_clients": total_clients,
        "total_online": total_online,
        "total_banquets": total_banquets,
        "total_cities": total_cities,
    }
    cache.set('site_counters', site_counters, timeout=0)
    return site_counters


def generate_random_number():
    current_hour = datetime.now().hour
    total_clients = Client.objects.count()

    if 12 <= current_hour <= 24 or 0 <= current_hour <= 2:
        random_number = randint(total_clients * 2, total_clients * 6)
    elif 8 <= current_hour <= 12:
        random_number = randint(10, total_clients * 2)
    else:
        random_number = randint(0, 7)

    return random_number


def get_total_cart_sum(request):
    total_cart_cost = 0

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            total_cart_cost = cart.total_cost()
    else:
        session_key = request.session.session_key
        cart = Cart.objects.filter(session_key=session_key).first()
        if cart:
            total_cart_cost = cart.total_cost()

    return {'total_cart_cost': str(total_cart_cost) + ' ₸'}
