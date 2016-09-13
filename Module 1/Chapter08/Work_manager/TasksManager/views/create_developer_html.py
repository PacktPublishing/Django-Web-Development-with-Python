from django.shortcuts import render
from django.http import HttpResponse
from TasksManager.models import Supervisor, Developer
# View for create_developer
def page(request):
    error = False
    # If form has posted
    if request.POST: 
      # This line checks if the data was sent in POST. If so, this means that the form has been submitted and we should treat it.
        if 'name' in request.POST: 
          # This line checks whether a given data named name exists in the POST variables.
            name = request.POST.get('name', '')
            # This line is used to retrieve the value in the POST dictionary. Normally, we perform filters to recover the data to avoid false data, but it would have required many lines of code.
        else:
            error=True
        if 'login' in request.POST:
            login = request.POST.get('login', '')
        else:
            error=True
        if 'password' in request.POST:
            password = request.POST.get('password', '')
        else:
            error=True
            supervisor_id = request.POST.get('supervisor', '')
        else:
            error=True
        if not error:
            # We must get the supervisor
            supervisor = Supervisor.objects.get(id = supervisor_id)
            new_dev = Developer(name=name, login=login, password=password, supervisor=supervisor)
            new_dev.save()
            return HttpResponse("Developer added")
        else:
            return HttpResponse("An error as occured")
    else:
        supervisors_list = Supervisor.objects.all()
        return render(request, 'en/public/create_developer.html', {'supervisors_list':supervisors_list})