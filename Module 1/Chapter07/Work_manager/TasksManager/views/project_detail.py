# -*- Coding: utf-8 -*-
from TasksManager.models import Project
from django.shortcuts import render
def page(request, pk):
	project = Project.objects.get(id=pk)
	return render(request, 'en/public/project_detail.html', {'project' : project})