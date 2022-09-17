from django.shortcuts import render
from projects.models import Project, Task
from django.contrib.auth.decorators import login_required

# Create your views here.

def project_view(request):
    projects = Project.objects.all().order_by("id")

    context = {
        'projects' : projects,
    }
    return render(request, "views/index.html", context)

@login_required
def users_view(request):
    my_projects = Project.objects.filter(assign = request.user.id).order_by("id")
    my_tasks = Task.objects.filter(assign = request.user.id).order_by("id")

    context = {
        'projects' : my_projects,
        'tasks' : my_tasks,
    }
    return render(request, "views/user-view.html", context)