from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^admin/', include(admin.site.urls)),
    url (r'^$', 'TasksManager.views.index.page'),
    url (r'^index$', 'TasksManager.views.index.page', name="public_index"),
    url (r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),
)
