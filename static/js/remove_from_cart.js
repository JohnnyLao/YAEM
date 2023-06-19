document.addEventListener('DOMContentLoaded', function() {
    // Найти все кнопки/ссылки удаления товара
    var removeButtons = document.getElementsByClassName('remove-item');

    // Привязать обработчик события клика для каждой кнопки/ссылки
    Array.from(removeButtons).forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();  // Предотвращение перехода по ссылке или отправки формы

            var productId = this.getAttribute('data-product-id');
            removeProduct(productId);
        });
    });

    // Функция для отправки AJAX-запроса на удаление товара
    function removeProduct(productId) {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/cart/remove/', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                // Успешно удалено, обновить отображение списка товаров
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    // Обновить отображение списка товаров, например, удалить соответствующий элемент DOM
                    var itemToRemove = document.querySelector('[data-product-id="' + productId + '"]');
                    if (itemToRemove) {
                        itemToRemove.parentNode.removeChild(itemToRemove);
                    }
                } else {
                    console.log('Ошибка удаления товара');
                }
            }
        };
        xhr.send('product_id=' + encodeURIComponent(productId));
    }
});
