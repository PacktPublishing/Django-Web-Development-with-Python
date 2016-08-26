from django.views.generic import DetailView
from TasksManager.models import Developer, Task

class Developer_detail(DetailView): 
	model=Developer
	template_name = 'en/public/developer_detail.html'
	def get_context_data(self, **kwargs):
	    # This overrides the get_context_data() method.
	    context = super(Developer_detail, self).get_context_data(**kwargs) 
	    # This allows calling the method of the super class. Without this line we would not have the basic context.
	    tasks_dev = Task.objects.filter(developer = self.object) 
	    # This allows us to retrieve the list of tasks developer. We use self.object, which is a Developer type object already defined by the DetailView class.
	    context['tasks_dev'] = tasks_dev 
	    # In this line, we add the task list to the context.
	    return context