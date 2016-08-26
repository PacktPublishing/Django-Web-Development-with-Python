from django.views.generic.list import ListView 
# In this line, we import the ListView class
from TasksManager.models import Project

class Project_list(ListView): 
	# In this line, we create a class that extends the ListView class.
	model=Project
	template_name = 'en/public/project_list.html' 
	# In this line, we define the template_name the same manner as in the urls.py file.
	paginate_by = 5 
	# In this line, we define the number of visible projects on a single page.
	def get_queryset(self): 
		# In this line, we override the get_queryset() method to return our queryset.
		queryset=Project.objects.all().order_by("title")
		return queryset