from django.urls import path

from cart.views import (AddToCart, CartClearView, RemoveFromCart,
                        RemoveFromCartOnCartPage, ViewCartPage)

app_name = "cart"

urlpatterns = [
    # add to cart
    path("add_to_cart/<int:product_id>", AddToCart.as_view(), name="add_to_cart"),
    # remove from cart
    path(
        "remove_from_cart/<int:product_id>",
        RemoveFromCart.as_view(),
        name="remove_from_cart",
    ),
    path(
        "remove_on_cart_page/",
        RemoveFromCartOnCartPage.as_view(),
        name="remove_on_cart_page",
    ),
    # cart page
    path("cart/", ViewCartPage.as_view(), name="cart_page"),
    path("cart/clear/", CartClearView.as_view(), name="cart_clear"),
]
