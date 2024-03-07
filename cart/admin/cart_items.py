from django.contrib import admin

from cart.models import CartItems


class CartItemsInlineAdmin(admin.TabularInline):
    model = CartItems
    extra = 0
    readonly_fields = ('dish', 'quantity', 'dish_price', 'subtotal')

    def subtotal(self, obj):
        return obj.subtotal()

    subtotal.short_description = 'Промежуточная стоимость'

    def dish_price(self, obj):
        return obj.dish.actual_price

    dish_price.short_description = 'Стоимость'
