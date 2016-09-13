jQuery(function($) {
    $('.object_list').jscroll({
        loadingHtml: '<img src="' + settings.STATIC_URL + 'site/img/loading.gif" alt="Loading" />',
        padding: 100,
        pagingSelector: '.pagination',
        nextSelector: 'a.next_page:last',
        contentSelector: '.item,.pagination'
    });
})