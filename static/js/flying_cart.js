    $(window).scroll(function() {
        if ($(this).scrollTop() >= 500) {
            $('#Cart').fadeIn();
        } else {
            $('#Cart').fadeOut();
        }
    });
