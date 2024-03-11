from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from banquets.models import BanquetCard
from cart.models import Cart
from main.models import Category, Client, Dish, Food_type


class Menu(TemplateView):
    template_name = "main/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs["url_name"]
        client = get_object_or_404(Client, url_name=url_name)
        categories = Category.objects.all().order_by("z_index")
        client_has_banquet = BanquetCard.objects.filter(client=client).exists()
        dishes = (
            Dish.objects.select_related("client")
            .prefetch_related("food_type")
            .filter(client=client)
            .order_by("z_index")
        )
        food_type = (
            Food_type.objects.filter(dish__in=dishes).distinct().order_by("z_index")
        )
        kitchen = (
            Food_type.objects.filter(dish__in=dishes)
            .filter(category__name="Кухня")
            .order_by("z_index")
            .distinct()
        )
        bar = (
            Food_type.objects.filter(dish__in=dishes)
            .filter(category__name="Бар")
            .order_by("z_index")
            .distinct()
        )
        # dish quantity
        user_cart = None
        if self.request.user.is_authenticated:
            user_cart = Cart.objects.filter(user=self.request.user).first()
        else:
            user_cart = Cart.objects.filter(
                session_key=self.request.session.session_key
            ).first()

        cart_items = {}
        if user_cart:
            for cart_item in user_cart.cart_items.all():
                cart_items[cart_item.dish.id] = cart_item.quantity

        context["dishes"] = dishes
        context['cart_items'] = cart_items
        context["food_type"] = food_type
        context["categories"] = categories
        context["client"] = client
        context["client_has_banquet"] = client_has_banquet
        context['kitchen'] = kitchen
        context['bar'] = bar

        # context['kitchen_menus'] = Food_type.objects.filter(category__name="Кухня")
        # context['bar_menus'] = Food_type.objects.filter(category__name="Бар")

        return context
