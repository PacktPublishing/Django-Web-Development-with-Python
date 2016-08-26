from TasksManager.models import Task
from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
# We import the csrf_exempt decorator that we will use to line 4.
import json
# We import the json module we use to line 8.
class Form_task_delete(forms.Form):
	# We create a form with a task field that contains the identifier of the task. When we create a form it allows us to use the Django validators to check the contents of the data sent by AJAX. Indeed, we are not immune that the user sends data to hack our server.
	task = forms.IntegerField()

@csrf_exempt
# This line allows to not verify the CSRF token for this view. Indeed, with AJAX we cannot reliably use the CSRF protection.
def page(request):
	return_value="0"
	# We create a variable named return_value that will contain a code returned to our JavaScript function. We initialize the value 0 to the variable.
	if len(request.POST) > 0:
		form = Form_task_delete(request.POST)
		if form.is_valid():
		# This line allows us to verify the validity of the value sent by the AJAX request.
			id_task = form.cleaned_data['task']
			task_record = Task.objects.get(id = id_task)
			task_record.delete()
			return_value=id_task
			# If the task been found, the return_value variable will contain the value of the id property after removing the task. This value will be returned to the JavaScript function and will be useful to remove the corresponding row in the HTML table.
	# The following line contains two significant items. The json.dumps() function will return a serialized JSON object. Serialization allows encoding an object sequence of characters. This technique allows different languages to share objects transparently. We also define a content_type to specify the type of data returned by the view.
	return HttpResponse(json.dumps(return_value), content_type = "application/json")