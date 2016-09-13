jQuery(function($) {
    var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
    var $image_upload_widget = $('#image_upload_widget');
    var current_image_path = $('#id_picture_path').val();
    if (current_image_path) {
        $('.preview', $image_upload_widget).html('<img src="' + window.settings.MEDIA_URL + current_image_path  + '" alt="" />');
    }
    var options = $.extend(window.translatable_file_uploader_options, {
        allowedExtensions: ['jpg', 'jpeg', 'gif', 'png'],
        action: window.ajax_uploader_path,
        element: $('.uploader', $image_upload_widget)[0],
        multiple: false,
        onComplete: function(id, fileName, responseJSON) {
            if(responseJSON.success) {
                $('.messages', $image_upload_widget).html("");
                // set the original to media_file_path
                $('#id_picture_path').val('uploads/' + fileName);
                // show preview link
                $('.preview', $image_upload_widget).html('<img src="' + window.settings.MEDIA_URL + 'uploads/' + fileName  + '" alt="" />');
            }
        },
        onAllComplete: function(uploads) {
            // uploads is an array of maps
            // the maps look like this: {file: FileObject, response: JSONServerResponse}
            $('.qq-upload-success').fadeOut("slow", function() {
                $(this).remove();
            });
        },
        params: {
            'csrf_token': csrfmiddlewaretoken,
            'csrf_name': 'csrfmiddlewaretoken',
            'csrf_xname': 'X-CSRFToken'
        },
        showMessage: function(message) {
            $('.messages', $image_upload_widget).html('<div class="alert alert-danger">' + message + '</div>');
        }
    });
    var uploader = new qq.FileUploader(options);
    $('.qq-delete-button', $image_upload_widget).click(function() {
        $('.messages', $image_upload_widget).html("");
        $('.preview', $image_upload_widget).html("");
        $('#id_delete_picture').val(1);
        return false;
    });
});