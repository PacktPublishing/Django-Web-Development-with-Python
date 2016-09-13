(function($) {
    $(document).on('click', '.like-button', function() {
        var $button = $(this);
        var $badge = $button.closest('.like-widget').find('.like-badge');
        $.post($button.data('href'), function(data) {
            if (data['action'] == 'added') {
                $button.addClass('active').html('<span class="glyphicon glyphicon-star"></span> ' + $button.data('unlike-text'));
            } else {
                $button.removeClass('active').html('<span class="glyphicon glyphicon-star-empty"></span> ' + $button.data('like-text'));
            }
            $badge.html(data['count']);
        }, 'json');
    });
})(jQuery);