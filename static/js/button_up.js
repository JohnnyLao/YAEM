//button up
$(window).scroll(function() {
        if ($(this).scrollTop() >= 1000) {
            $('#scrollToTopButton').fadeIn();
            $('#scrollToTopButton').addClass('animated-button');
        } else {
            $('#scrollToTopButton').fadeOut();
            $('#scrollToTopButton').removeClass('animated-button');
        }
    });