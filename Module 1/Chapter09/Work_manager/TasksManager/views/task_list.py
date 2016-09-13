# -*- Coding: utf-8 -*-
from django.shortcuts import render
from TasksManager.models import Task
def page(request):
	tasks_list = Task.objects.all() 
	# This line is used to retrieve all existing tasks database.
	last_task = 0 
	# In this line, we define last_task variable with a null value without generating a bug when using the render() method.
	if 'last_task' in request.session: 
	# This line is used to check whether there is a session variable named last_task.
		last_task = Task.objects.get(id = request.session['last_task'])
		# In this line, we get the recording of the last task in our last_task variable.
		tasks_list = tasks_list.exclude(id = request.session['last_task'])
		# In this line, we exclude the last task for the queryset to not have duplicates.
	return render(request, 'en/public/tasks_list.html', {'tasks_list': tasks_list, 'last_task' : last_task})