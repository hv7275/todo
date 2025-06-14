from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'list/index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    else:
        form = TaskForm()
    return render(request, 'list/add_list.html', {'form': form})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'list/update.html', {'form': form})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo-home')
