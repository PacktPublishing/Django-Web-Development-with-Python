# -*- Coding: utf-8 -*-
from django.shortcuts import render
from TasksManager.models import Project
# View for index page. 
def page(request):
	# new_project = Project(title="Tasks Manager with Django", description="Django project to getting start with Django easily.", client_name="Me") 
	# new_project.save()
	# all_projects = Project.objects.all()
	action = 'Display project with client name = "Me"'
	projects_to_me = Project.objects.filter(client_name="Me")
	first_project = Project.objects.get(id="1")
	queryset_project = Project.objects.filter(client_name="Me").order_by("id")
	project = Project.objects.filter(client_name="Me").order_by("id")[:1].get()
	
	return render(request, 'en/public/index.html', {'action':action, 'projects_to_me': projects_to_me})