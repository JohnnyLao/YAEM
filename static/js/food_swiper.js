document.addEventListener('DOMContentLoaded', function () {
    var foodTypeSwiper = new Swiper('#foodTypeSwiper', {
        slidesPerView: 'auto',
        spaceBetween: 10,
        freeMode: true,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        allowTouchMove: true // Разрешаем свайп слайдов
    });

    var foodTypeButtons = document.querySelectorAll('.food-type-button');
    var foodTypeSections = document.querySelectorAll('.food-type-section');

    console.log(foodTypeButtons);
    console.log(foodTypeSections);

    function setActiveButton(sectionId) {
        foodTypeButtons.forEach(function (btn) {
            btn.classList.remove('active');
            if (btn.getAttribute('data-target') === sectionId) {
                btn.classList.add('active');
            }
        });
    }

    function scrollToSection(sectionId) {
        var targetElement = document.getElementById(sectionId);
        if (targetElement) {
            var targetOffsetTop = targetElement.offsetTop;
            window.scrollTo({ top: targetOffsetTop, behavior: 'smooth' });
            setActiveButton(sectionId);
        }
    }

    function onScroll() {
        var currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        for (var i = 0; i < foodTypeSections.length; i++) {
            var section = foodTypeSections[i];
            if (section.offsetTop <= currentScroll + 30 && section.offsetTop + section.offsetHeight > currentScroll + 50) {
                setActiveButton(section.getAttribute('id'));
                break;
            }
        }
    }

    window.addEventListener('scroll', function () {
        onScroll();
    });

    foodTypeButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            var target = event.currentTarget.getAttribute('data-target');
            scrollToSection(target);
        });
    });

    foodTypeSwiper.on('slideChange', function () {
        var activeSlide = foodTypeSwiper.slides[foodTypeSwiper.activeIndex];
        var sectionId = activeSlide.getAttribute('data-food');
        scrollToSection(sectionId);
    });

    // Предотвращаем распространение события свайпа, чтобы оно не вызывало прокрутку страницы
    foodTypeSwiper.el.addEventListener('touchmove', function (e) {
        e.stopPropagation();
    });

    setActiveButton(foodTypeSections[0].getAttribute('id'));
});
