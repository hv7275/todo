from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):
    query = request.GET.get('q', '').strip()
    if query != '':
        tasks = Task.objects.filter(user=request.user, title__icontains=query)
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'list/index.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo-home')
    else:
        form = TaskForm()
    return render(request, 'list/add_list.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user != request.user:
        return redirect('todo-home')
    
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'list/update.html', {'form': form})
@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.user == request.user:
        task.delete()
    return redirect('todo-home')
