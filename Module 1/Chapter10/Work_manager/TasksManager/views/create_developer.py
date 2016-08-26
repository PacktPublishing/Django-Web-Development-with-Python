from django.shortcuts import render
from django.http import HttpResponse
from TasksManager.models import Supervisor, Developer
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class Form_inscription(forms.Form):
	name     = forms.CharField(label="Name", max_length=30, initial="new")
	login    = forms.CharField(label = "Login")
	password = forms.CharField(label = "Password", widget = forms.PasswordInput)
	password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput) 
	supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all())
	def clean(self): 
		cleaned_data = super(Form_inscription, self).clean()
		password = self.cleaned_data.get('password') 
		password_bis = self.cleaned_data.get('password_bis')
		if password and password_bis and password != password_bis:
			raise forms.ValidationError("Passwords are not identical.") 
		return self.cleaned_data
# View for create_developer
@login_required
def page(request):
	if request.POST:
		form = Form_inscription(request.POST)
		if form.is_valid():
			name          = form.cleaned_data['name']
			login         = form.cleaned_data['login']
			password      = form.cleaned_data['password']
			supervisor    = form.cleaned_data['supervisor'] 
			new_user = User.objects.create_user(username = login, password=password)
			new_user.is_active = True
			new_user.last_name=name
			new_user.save()
			new_developer = Developer(user_auth = new_user, supervisor=supervisor)
			new_developer.save()
			return HttpResponse("Developer added")
		else:
			return render(request, 'en/public/create_developer.html', {'form' : form})
	else:
		form = Form_inscription()
		return render(request, 'en/public/create_developer.html', {'form' : form})