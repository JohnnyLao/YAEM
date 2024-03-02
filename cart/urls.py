from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    # cart page
    path('<slug:establishment_url_name>/cart', views.CartPage.as_view(), name='cart_page'),
    # add to cart
    # path('add/<int:dish_id>', views.add_to_cart, name='add'),
    path('add/', views.add_to_cart, name='add'),
    # remove from cart
    # path('remove/<int:dish_id>', views.remove_from_cart, name='remove'),
    path('remove/', views.remove_from_cart, name='remove'),
    # clear cart
    path('clear/', views.cart_remove, name='clear'),
]
