from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import List_model
from .forms import UserTodoList

def main_page(request):
    return render(request, 'main_page.html')

class TodoListView(View):
    def get(self, request):
        form = UserTodoList()
        todos = List_model.objects.filter(user=request.user)
        return render(request, 'todo_page.html', {
            'form': form,
            'todos': todos,
        })

    def post(self, request):
        form = UserTodoList(request.POST)
        if form.is_valid():
            todo = List_model(
                user=request.user,
                day_tasks=form.cleaned_data['day_tasks'],
                prioritet=form.cleaned_data['prioritet'],
                completed_task=form.cleaned_data['completed_task'],
            )
            todo.save()
            return redirect('/to-do/')

        todos = List_model.objects.filter(user=request.user)
        return render(request, 'todo_page.html', {
            'form': form,
            'todos': todos,
        })

class ToggleTaskCompletionView(View):
    def post(self, request, task_id):
        task = get_object_or_404(List_model, id=task_id, user=request.user)
        task.completed_task = not task.completed_task 
        task.save()
        return redirect('/to-do/')
