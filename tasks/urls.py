from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list),
    path('tasks/add/', views.add_task),
    path('tasks/<int:task_id>/update/', views.update_task),
    path('tasks/<int:task_id>/delete/', views.delete_task),
]