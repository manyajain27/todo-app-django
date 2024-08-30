from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm 
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

#view all tasks
def view_all_tasks(request):
    tasks=Task.objects.filter(completed=False)
    completed_tasks=Task.objects.filter(completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks
        }
    return render(request,'home.html',context)

def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed})

#view details of each task
def view_details(request,pk):
    task=get_object_or_404(Task,pk=pk)
    context={'task':task}
    return render(request,'task_details.html',context)

#creating anew task
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    context={'form':form}
    return render(request, 'task_edit.html', context)

#updating/editing tasks
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list') 
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

#deleting tasks
@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list') 