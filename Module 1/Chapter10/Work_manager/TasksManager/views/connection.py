from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
# This line allows you to import the necessary functions of the authentication module.
def page(request):
	if request.POST:
	# This line is used to check if the Form_connection form has been posted. If mailed, the form will be treated, otherwise it will be displayed to the user.
		form = Form_connection(request.POST) 
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			# This line verifies that the username exists and the password is correct.
			if user:
				# In this line, the authenticate function returns None if authentication has failed, otherwise it returns an object that validate the condition.
				login(request, user)
				# In this line, the login() function allows the user to connect.
				if request.GET.get('next') is not None:
					return redirect(request.GET['next'])

		else:
			return render(request, 'en/public/connection.html', {'form' : form})
	else:
		form = Form_connection()
	return render(request, 'en/public/connection.html', {'form' : form})
class Form_connection(forms.Form):
	username = forms.CharField(label="Login")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	def clean(self):
		cleaned_data = super(Form_connection, self).clean()
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not authenticate(username=username, password=password):
			raise forms.ValidationError("Wrong login or passwsord")
		return self.cleaned_data
