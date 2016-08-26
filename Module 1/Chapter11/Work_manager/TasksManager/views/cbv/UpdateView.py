from django.views.generic import UpdateView
from TasksManager.models import Task
from django.forms import ModelForm
from django.core.urlresolvers import reverse

class Form_task_time(ModelForm): 
	# In this line, we create a form that extends the ModelForm. The UpdateView and CreateView CBV are based on a ModelForm system.
	class Meta:
		model = Task
		fields = ['time_elapsed'] 
		# It is used to define the fields that appear in the form. Here there will be only one field.

class Task_update_time(UpdateView):
	model = Task
	template_name = 'en/public/update_task_developer.html'
	form_class = Form_task_time 
	# In this line, we impose your CBV to use the ModelForm we created. When you do not define this line, Django automatically generates a ModelForm.
	success_url = 'public_index' 
	# This line sets the name of the URL that will be seen once the change has been completed.
	def get_success_url(self): 
		# In this line, when you put the name of a URL in the success_url property, we have to override this method. The reverse() method returns the URL corresponding to a URL name.
		return reverse(self.success_url)
