from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    # cart page
    path('<slug:establishment_url_name>/cart', views.CartPage.as_view(), name='cart_page'),
    # add to cart
    path('add/<int:dish_id>', views.add_to_cart, name='add'),
]
