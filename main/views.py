from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import add_task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'main/task_list.html', {'tasks': tasks})
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'main/details.html', {'task': task})
def create_task(request):  # Renamed from add_task to create_task
    if request.method == 'POST':
        form = add_task(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assuming Task model has a user field
            task.save()
            return redirect('task_list')
    else:
        form = add_task()
    return render(request, 'main/add_task.html', {'form': form})
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = add_task(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = add_task(instance=task)
    return render(request, 'main/edit_task.html', {'form': form})
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'main/delete_task.html', {'task': task})
