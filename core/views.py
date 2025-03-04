from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CreateTaskForm
from django.contrib import messages
from core.models import Task
from django.utils import timezone

# Create your views here.
def list_task(request):
    tasks = Task.objects.all().order_by('-id')
    context = {
        "tasks" : tasks
    }

    return render(
        request=request,
        template_name= "todo/list_task.html",
        context=context
        )

def create_task(request):

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Task created sucessfully")
            return redirect('todo:create')
    else:
        form = CreateTaskForm()

    context = {"form": form}
    return render(
        request=request,
        template_name="todo/create_form.html",
        context=context
        )


def change_status(request, id):

    task= get_object_or_404(klass=Task, pk=id)
    task.status = "completed"
    task.finished_at = timezone.now()
    task.save()
    return redirect('todo:list')

def delete_task(request,id):
    task= get_object_or_404(klass=Task, pk=id)
    task.delete()
    return redirect('todo:list')


def detail_task(request, id):
    task= get_object_or_404(klass=Task, pk=id)
    context = {
        "task" : task
    }

    return render(
        request=request,
        template_name= "todo/detail_task.html",
        context=context
        )

def update_task(request, id):

    task= get_object_or_404(klass=Task, pk=id)

    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Task updated sucessfully")
            return redirect('todo:list')
    else:
        form = CreateTaskForm(instance=task)

    context = {"form": form,
               "task": task}
    return render(
        request=request,
        template_name="todo/update_task.html",
        context=context
        )