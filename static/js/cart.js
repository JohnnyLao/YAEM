<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
    $(".add-to-cart-form").on("submit", function(event) {
        event.preventDefault();
        
        var form = $(this);
        var dishId = form.data("dish-id");
        var quantity = form.find("input[name='quantity']").val();
        
        $.ajax({
            url: form.attr("action"),
            type: form.attr("method"),
            data: {
                dish_id: dishId,
                quantity: quantity
            },
            success: function(response) {
                // Обновление информации в корзине без перезагрузки страницы
                updateCartInfo(response);
            },
            error: function(xhr, status, error) {
                console.log("An error occurred: " + error);
            }
        });
    });
    
    function updateCartInfo(response) {
        // Обновление информации в корзине на странице
        var cartInfoElement = $(".cart-info");
        var cartTotalPriceElement = $(".cart-total-price");
        
        // Обновление количества товаров в корзине
        cartInfoElement.text(response.cart_info);
        
        // Обновление общей стоимости корзины
        cartTotalPriceElement.text(response.cart_total_price);
    }
});
</script>
