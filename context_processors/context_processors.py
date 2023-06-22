from main.models import Dish, Client


def data_counter_site(request):
    total_dishes = Dish.objects.count()
    total_clients = Client.objects.count()
    total_orders = total_dishes * 21

    return {
        'total_dishes': total_dishes,
        'total_clients': total_clients,
        'total_orders': total_orders,
    }