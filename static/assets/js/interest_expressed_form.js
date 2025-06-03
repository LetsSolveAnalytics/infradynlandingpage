$(document).ready(function () {
    $('#mc-form').on('submit', function(e) {
        e.preventDefault();

        const email = $('#mc-email').val();
        const csrfToken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url:  $('#mc-form').data('url'),
            data: {
                email: email,
                csrfmiddlewaretoken: csrfToken
            },
            success: function(response) {
                const msgBox = $('#feedback-message');
                msgBox.removeClass('alert-success alert-danger').hide();

                if (response.status === 'success') {
                    msgBox.addClass('alert alert-success').text(response.message).fadeIn();
                    $('#mc-form')[0].reset(); // optional: clear form
                } else {
                    msgBox.addClass('alert alert-danger').text(response.message).fadeIn();
                }
            },
            error: function() {
                $('#feedback-message').removeClass().addClass('alert alert-danger').text('An unexpected error occurred.').fadeIn();
            }
        });
    });
});