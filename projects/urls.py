from django.urls import path
from . import views
app_name = 'projects'

urlpatterns = [
    path('', views.projects, name="projects"),
    path('create-project/', views.CreateProject, name='create-project'),
    path('create-task/', views.CreateTask, name='create-task'),
    path('project-detail/<int:id>/', views.ProjectDetail, name='project-detail'),
    path('update-project/<int:id>/', views.UpdateProject, name='update-project'),
    path('update-task/<int:id>/', views.UpdateTask, name='update-task'),
]
