<script>
    $(document).ready(function() {
        $("form.add-to-cart-form").submit(function(e) {
            e.preventDefault();
            var form = $(this);
            var url = form.attr('action');
            var formData = new FormData(form[0]);

            // Отключаем кнопку добавления
            var addButton = form.find('button[type="submit"]');
            addButton.prop('disabled', true);

            $.ajax({
                type: 'POST',
                url: url,
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    if (response.success) {
                        // Обновление информации о корзине
                        $("#cart-info").text("Количество товаров в корзине: " + response.cart_count);
                    }
                    else {
                        // Обработка ошибки
                        alert(response.error);
                    }
                },
                complete: function() {
                    // Включаем кнопку добавления после завершения AJAX-запроса
                    addButton.prop('disabled', false);
                }
            });
        });
    });
</script>
