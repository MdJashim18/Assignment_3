from django.shortcuts import render,redirect
from task.forms import TaskForm
from .import models,forms
from task.models import TaskModel
# Create your views here.

def task(request):
    if request.method=='POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Show_task')
    else:
        form = forms.TaskForm()
    return render(request,'task.html',{'form' : form})

def Edit_task(request,id):
    task = models.TaskModel.objects.get(pk=id)
    form = forms.TaskForm(instance=task)
    if request.method=='POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Show_task')
    else:
        form = forms.TaskForm()
    return render(request,'task.html',{'form' : form})

def delete_task(request,id):
    form = models.TaskModel.objects.get(pk=id)
    form.delete()
    return redirect('Show_task')

def Show_task(request):
    tasks = TaskModel.objects.prefetch_related('categories').all()
    return render(request,'show.html',{'tasks' : tasks})

def complete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.is_completed = True  
    task.save()
    return redirect('Show_task')