from django.core.urlresolvers import reverse
from django.views.generic import DeleteView
from TasksManager.models import Task

class Task_delete(DeleteView):
	model = Task
	template_name = 'en/public/confirm_delete_task.html'
	success_url = 'public_index'
	def get_success_url(self):
		return reverse(self.success_url)