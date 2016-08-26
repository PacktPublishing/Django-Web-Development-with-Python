from django.shortcuts import render
from TasksManager.models import Project
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class Form_project_create(forms.Form):
	title = forms.CharField(label="Title", max_length=30)
	description = forms.CharField(widget= forms.Textarea(attrs={'rows': 5, 'cols': 100,}))
	client_name = forms.CharField(label="Client", max_length=50)
	
def page(request):
	if request.POST:
		form = Form_project_create(request.POST)
		if form.is_valid(): 
			title = form.cleaned_data['title'] 
			description = form.cleaned_data['description']
			client_name = form.cleaned_data['client_name']
			new_project = Project(title=title, description=description, client_name=client_name)
			new_project.save()
			return HttpResponseRedirect(reverse('public_index')) 
		else:
			return render(request, 'en/public/create_project.html', {'form' : form}) 
	else:
		form = Form_project_create() 
	return render(request, 'en/public/create_project.html', {'form' : form})