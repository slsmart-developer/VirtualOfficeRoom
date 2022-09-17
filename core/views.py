from django.shortcuts import render
from django.shortcuts import render
from projects.models import Project, Task

# Create your views here.
def dashboard(request):
    res = {}
    projects = Project.objects.all().count()
    task = Task.objects.all().count()
    active_proeject = Project.objects.filter(status__in = ["2", "3"]).count()
    res["project"] = projects
    res["task"] = task
    res["active_proeject"] = active_proeject
    return render(request, "core/dashboard.html", context=res)