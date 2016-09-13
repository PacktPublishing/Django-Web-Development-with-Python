# -*- Coding: utf-8 -*-
from django.shortcuts import render
from TasksManager.models import Project, Task
from django.db.models import Q
# View for index page. 
def page(request):
	return render(request, 'en/public/index.html')