from django.views.generic import UpdateView
from django.core.urlresolvers import reverse

class UpdateViewCustom(UpdateView):
	template_name = 'en/cbv/UpdateViewCustom.html' 
	# In this line, we define the template that will be used for all the CBV that extends the UpdateViewCustom class. This template_name field can still be changed if we need it.
	url_name="" 
	# This line is used to create the url_name property. This property will help us to define the name of the current URL. In this way, we can add the link in the action attribute of the form.
	def get_success_url(self):
		# In this line, we override the get_success_url() method by default, this method uses the name URLs.
		return reverse(self.success_url)
	def get_context_data(self, **kwargs): 
		# This line is the method we use to send data to the template.
		context = super(UpdateViewCustom, self).get_context_data(**kwargs) 
		# In this line, we perform the super class method to send normal data from the CBV UpdateView.
		model_name = self.model._meta.verbose_name.title() 
		# In this line, we get the verbose_name property of the defined model.
		context['model_name'] = model_name 
		# In this line, we send the verbose_name property to the template.
		context['url_name'] = self.url_name \
		# This line allows us to send the name of our URL to the template.
		return context