from datetime import date, datetime

from django.contrib.auth import get_user_model
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
        # get establishment info
        client = get_object_or_404(Client, url_name=url_name)
        categories = client.get_categories.prefetch_related(
            'get_subcategories__get_dishes'
        ).all()
        food_types = []
        dishes = []
        for category in categories:
            subcategories = category.get_subcategories.all()
            food_types.extend(subcategories)
            for food_type in subcategories:
                dish = food_type.get_dishes.filter(stop=False)
                dishes.extend(dish)

        client_has_banquet = BanquetCard.objects.filter(client=client).exists()
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
        client_date = client.paid_at
        today_date = datetime.now().date()

        context = {'client_date': client_date, 'today_date': today_date}
        context["dishes"] = dishes
        context['cart_items'] = cart_items
        context["food_type"] = food_types
        context["categories"] = categories
        context["client"] = client
        context["client_has_banquet"] = client_has_banquet

        return context
