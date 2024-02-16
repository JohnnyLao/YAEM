
    document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('#foodTypeSwiper', {
        slidesPerView: 'auto',
        spaceBetween: 0,
        on: {
            slideChangeTransitionEnd: function () {
                // При изменении слайда свайпера, просто обновляем активную категорию, но не подсвечиваем
                updateActiveFoodType();
            },
        },
    });

    var currentActiveIndex = 0; // Переменная для отслеживания текущей активной категории

    function updateActiveFoodType() {
        var activeIndex = swiper.activeIndex;
        currentActiveIndex = activeIndex;
    }

    function highlightActiveFoodType() {
        var buttons = document.querySelectorAll('.food-type-button');
        buttons.forEach(function (button, index) {
            if (index === currentActiveIndex) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });
    }

    // Вызовем эту функцию при загрузке страницы, чтобы установить начальное состояние
    updateActiveFoodType();
    highlightActiveFoodType();

    // Обработчик события прокрутки страницы
    window.addEventListener('scroll', function () {
        highlightActiveCategoryOnScroll();
    });

    function highlightActiveCategoryOnScroll() {
        var categories = document.querySelectorAll('.food-type-button');
        var scrollPosition = window.scrollY;
        var foundActive = false;

        categories.forEach(function (category, index) {
            var targetId = category.getAttribute('data-target');
            var targetSection = document.getElementById(targetId);

            if (!foundActive && targetSection.offsetTop <= scrollPosition && targetSection.offsetTop + targetSection.offsetHeight > scrollPosition) {
                // Проверяем, чтобы не было двух активных категорий
                if (index !== currentActiveIndex) {
                    removeActiveClass();
                    category.classList.add('active');

                    // Перемещаем свайпер к текущей категории
                    swiper.slideTo(index);
                    currentActiveIndex = index; // Обновляем текущую активную категорию
                }
                foundActive = true;
            }
        });

        // Если не найдено активной категории при прокрутке, обновляем активную категорию, чтобы избежать ошибок
        if (!foundActive) {
            updateActiveFoodType();
        }
    }

    function removeActiveClass() {
        var categories = document.querySelectorAll('.food-type-button');
        categories.forEach(function (category) {
            category.classList.remove('active');
        });
    }
});