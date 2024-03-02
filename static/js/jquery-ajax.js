    $(document).ready(function () {
        $(document).on("click", ".add-to-cart", function (e) {
            e.preventDefault();
            var dish_id = $(this).data('dish-id');
            var add_to_cart_url = $(this).attr("href");
            var quantitySpan = $(this).siblings('.cart-quantity');
            var subtotal = $('.cart-subtotal-value[data-dish-id="' + dish_id + '"]');
            var totalSpan = $('.cart-total-value');

            $.ajax({
                url: add_to_cart_url,
                method: 'POST',
                data: {'dish_id': dish_id},
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                success: function(data) {
                    if (data.success) {
                        var currentQuantity = parseInt(quantitySpan.text());
                        quantitySpan.text(currentQuantity + 1);
                        subtotal.text(data.subtotal + ' ₸');
                        totalSpan.text(data.total + ' ₸');
                    }
                }
            });
        });


        $(document).on("click", ".remove-from-cart", function (e) {
            e.preventDefault();
            var dish_id = $(this).data('dish-id');
            var remove_from_cart_url = $(this).attr("href");
            var quantitySpan = $(this).siblings('.cart-quantity');
            var subtotal = $('.cart-subtotal-value[data-dish-id="' + dish_id + '"]');
            var totalSpan = $('.cart-total-value');

            $.ajax({
                url: remove_from_cart_url,
                method: 'POST',
                data: {'dish_id': dish_id},
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                success: function(data) {
                    if (data.success) {
                        var currentQuantity = parseInt(quantitySpan.text());
                        quantitySpan.text(Math.max(currentQuantity - 1, 0));
                        quantitySpan.toggle(Math.max(currentQuantity - 1, 0) >= 1);

                        var newSubtotal = data.new_subtotal;
                        subtotal.text(data.subtotal + ' ₸');
                        totalSpan.text(data.total + ' ₸');
                    }
                }
            });
        });
    });