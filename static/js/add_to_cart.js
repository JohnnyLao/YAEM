$(document).ready(function() {
        $(".add-to-cart-form").submit(function(e) {
            e.preventDefault();
            var form = $(this);
            var url = form.attr('action');
            var formData = new FormData(form[0]);

            $.ajax({
                type: 'POST',
                url: url,
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    // handle success response
                },
                error: function(xhr, status, error) {
                    // handle error response
                }
            });
        });
    });