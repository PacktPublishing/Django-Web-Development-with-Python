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
    url (r'^project-detail-(?P<pk>\d+)$', 'TasksManager.views.project_detail.page', name="project_detail"),
    url(r'^create-developer$', 'TasksManager.views.create_developer.page', name="create_developer"),
    url(r'^create-supervisor$', 'TasksManager.views.create_supervisor.page', name="create_supervisor"),
    url(r'^create_project$', 'TasksManager.views.create_project.page', name='create_project'),
)
