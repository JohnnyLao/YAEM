$(document).ready(function () {
    // Функция для обновления интерфейса после изменения корзины
    function updateCartInterface(data, dish_id) {
        // Получаем элементы интерфейса для обновления
        var quantity = $('.cart-quantity[data-dish-id="' + dish_id + '"]');
        var subtotal = $('.cart-subtotal-value[data-dish-id="' + dish_id + '"]');
        var total = $('.cart-total-value');
        var cartElement = $('.cart-element[data-dish-id="' + dish_id + '"]');
        var minusButton = $('.remove-from-cart[data-dish-id="' + dish_id + '"]');
        var zeroQuantity = $('.zero-quantity[data-dish-id="' + dish_id + '"]');
        var totalCartCost = $('.total-cart-cost');
        var flyingCart = $('.flying-cart');

        // Обновляем значения в соответствии с данными из AJAX-запроса
        quantity.text(data.quantity);
        subtotal.text(data.subtotal + ' ₸');
        total.text(data.total + ' ₸');
        totalCartCost.text(data.total + ' ₸');

        if (parseInt(totalCartCost.text()) > 0) {
            flyingCart.removeClass('invisible');
        } else {
            flyingCart.addClass('invisible');
        }

        // Показываем или скрываем элементы в зависимости от количества товара
        if (parseInt(data.quantity) > 0) {
            minusButton.fadeIn();
            minusButton.removeClass('invisible');
            zeroQuantity.fadeIn();
        } else {
            minusButton.fadeOut();
            zeroQuantity.fadeOut();
            cartElement.fadeOut();
        }
    }

    // Обработчик события клика на элементы с классом "add-to-cart"
    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();
        var dish_id = $(this).data('dish-id');
        var add_to_cart_url = $(this).attr("href");

        // Выполняем AJAX-запрос для добавления товара в корзину
        $.ajax({
            url: add_to_cart_url,
            method: 'POST',
            data: {'dish_id': dish_id},
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            success: function (data) {
                if (data.success) {
                    // Обновляем интерфейс после успешного выполнения запроса
                    updateCartInterface(data, dish_id);
                }
            }
        });
    });

    // Обработчик события клика на элементы с классом "remove-from-cart"
    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();
        var removeLink = $(this);
        var dish_id = removeLink.data('dish-id');
        var remove_from_cart_url = removeLink.attr("href");

        // Выполняем AJAX-запрос для удаления товара из корзины
        $.ajax({
            url: remove_from_cart_url,
            method: 'POST',
            data: {'dish_id': dish_id},
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            success: function (data) {
                if (data.success) {
                    // Обновляем интерфейс после успешного выполнения запроса
                    updateCartInterface(data, dish_id);
                }
            }
        });
    });

    // Инициализация интерфейса корзины при загрузке страницы
    $(".add-to-cart").each(function () {
        var dish_id = $(this).data('dish-id');
        // Получаем количество товара для каждого продукта и обновляем интерфейс
        var quantity = $('.cart-quantity[data-dish-id="' + dish_id + '"]').text();
        if (parseInt(quantity) > 0) {
            var minusButton = $('.remove-from-cart[data-dish-id="' + dish_id + '"]');
            var zeroQuantity = $('.zero-quantity[data-dish-id="' + dish_id + '"]');
            minusButton.removeClass('invisible');
            zeroQuantity.fadeIn();

            var totalCartCost = parseFloat($('.total-cart-cost').text());
            var flyingCart = $('.flying-cart');
            if (totalCartCost > 0) {
                flyingCart.removeClass('invisible').fadeIn();
            }
        }
    });
});
