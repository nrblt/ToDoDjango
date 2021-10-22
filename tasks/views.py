from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task
from .forms import *
# Create your views here.

def index(request):
    obj=Task.objects.all()
    form=TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid()==True:
            form.save()
        return redirect('/')
    context={
        'object':obj,
        'form':form,
    }
    return render(request,'task/task_page.html',context)


def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form,
        'task':task
    }
    return render(request,'task/task_update.html',context)

def deleteTask(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('/');