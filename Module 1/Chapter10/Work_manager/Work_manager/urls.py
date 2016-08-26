from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.decorators import login_required

from TasksManager.models import Project, Task, Developer

from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from TasksManager.views.cbv.ListView import Project_list
from TasksManager.views.cbv.DetailView import Developer_detail
from TasksManager.views.cbv.UpdateView import Task_update_time
from TasksManager.views.cbv.UpdateViewCustom import UpdateViewCustom
from TasksManager.views.cbv.DeleteView import Task_delete


urlpatterns = patterns('',
	# url(r'^create_project$', 'TasksManager.views.create_project.page', name='create_project'),
	# url (r'^project_list$', ListView.as_view(model=Project, template_name="en/public/project_list.html"), name="project_list"),
	# url (r'^task_detail_(?P<pk>\d+)$', DetailView.as_view(model=Task, template_name="en/public/task_detail.html"), name="task_detail"),
	# url (r'^create_project$', CreateView.as_view(model=Project, template_name="en/public/create_project.html", success_url = 'index'), name="create_project"),
	# url (r'^update_task_(?P<pk>\d+)$', UpdateView.as_view(model=Task, template_name="en/public/update_task.html", success_url="index"), name="update_task"),
	
	url (r'^admin/', include(admin.site.urls)),
	url (r'^$', 'TasksManager.views.index.page', name="public_empty"),
	url (r'^index$', 'TasksManager.views.index.page', name="public_index"),
	url (r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),
	url (r'^logout$', 'TasksManager.views.logout.page', name="public_logout"),
	url (r'^project-detail-(?P<pk>\d+)$', 'TasksManager.views.project_detail.page', name="project_detail"),
	url(r'^create-developer$', 'TasksManager.views.create_developer.page', name="create_developer"),
	url(r'^create-supervisor$', 'TasksManager.views.create_supervisor.page', name="create_supervisor"),
	url (r'^create_project$', login_required(CreateView.as_view(model=Project, template_name="en/public/create_project.html", success_url = 'index')), name="create_project"),
	
	url (r'^create_task$', CreateView.as_view(model=Task, template_name="en/public/create_task.html", success_url = 'task_list'), name="create_task"),
	url (r'^project_list$', Project_list.as_view(), name="project_list"),
	url (r'^developer_list$', ListView.as_view(model=Developer, template_name="en/public/developer_list.html"), name="developer_list"),
	# url (r'^developer_detail_(?P<pk>\d+)$', Developer_detail.as_view(), name="developer_detail"),
	url (r'^update_task_time_(?P<pk>\d+)$', Task_update_time.as_view(), name = "update_task_time"),
	url(r'task_delete_(?P<pk>\d+)$', Task_delete.as_view(), name="task_delete"),
	url (r'^update_task_(?P<pk>\d+)$', UpdateViewCustom.as_view(model=Task, url_name="update_task", success_url="public_empty"), name="update_task"),
	url (r'^task_detail_(?P<pk>\d+)$', 'TasksManager.views.task_detail.page', name="task_detail"),
	url (r'^task_list$', 'TasksManager.views.task_list.page', name="task_list"),

)
