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
        client = get_object_or_404(Client, url_name=url_name)
        categories = Category.objects.filter(client=client, is_active=True)
        # food_types = (
        #     Food_type.objects.filter(category__in=categories).distinct()
        # )
        # dishes = (
        #     Dish.objects.filter(food_type__in=food_types)
        # )
        dishes = (
            Dish.objects.select_related("client")
            .prefetch_related("food_type")
            .filter(client=client, stop=False)
        )
        food_types = Food_type.objects.filter(dish__in=dishes).distinct()

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

        # -------------
        # user = get_user_model().objects.get(id=1)
        # print('User:', user)
        # establishments = user.get_user_establishments.all()
        # print('Est:', establishments)
        # for establishment in establishments:
        #     categories = establishment.get_categories.all()
        #     print('Cat:', categories)
        #
        #     for category in categories:
        #         subcategories = category.get_subcategories.all()
        #         print('SubCat:', subcategories)
        #
        #         for subcategory in subcategories:
        #             dishes = subcategory.get_dishes.all()
        #             print('Dish:', dishes)
        # -------------
        client_date = client.paid_at
        today_date = datetime.now().date()  # Получаем сегодняшнюю дату

        context = {'client_date': client_date, 'today_date': today_date}
        context["dishes"] = dishes
        context['cart_items'] = cart_items
        context["food_type"] = food_types
        context["categories"] = categories
        context["client"] = client
        context["client_has_banquet"] = client_has_banquet

        return context
