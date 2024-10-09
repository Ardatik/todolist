from django.urls import path
from .import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('to-do/', views.TodoListView.as_view(), name='to-do'),
    path('toggle-task-completion/<int:task_id>/',
         views.ToggleTaskCompletionView.as_view(), name='toggle_task_completion'),

]
