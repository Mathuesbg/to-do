from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CreateTaskForm, UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from core.models import Task
from django.utils import timezone

# Create your views here.
def list_task(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-id')
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
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
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


def register(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="User registered!")
            return redirect("todo:list")

    else:
        form = UserForm()

    return render(
        request=request,
        template_name= "todo/register.html",
        context= {
            'form':form
        }

    )


def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request=request, user=user)
            messages.success(request=request, message="successfully logged in!")
            return redirect("todo:list")

    else:    
        form = AuthenticationForm(request=request)

    return render(
        request=request,
        template_name="todo/login.html", 
        context= {
        "form" : form
        }
    )
    
def logout(request):
    auth.logout(request)
    return redirect("todo:login")