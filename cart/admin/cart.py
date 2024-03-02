from django.contrib import admin

from cart.admin.cart_items import CartItemsInlineAdmin
from cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_timestamp', 'total_dishes')
    list_display_links = ('id', 'user',)
    inlines = (CartItemsInlineAdmin,)

    def total_dishes(self, obj):
        total = sum(item.quantity for item in obj.cart_items.all())
        if total > 0:
            return total
        else:
            return 0
    total_dishes.short_description = 'Количество добавленных блюд'
