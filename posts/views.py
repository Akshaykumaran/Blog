from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, TaskForm

def home(request):
    projects = Project.objects.all()
    return render(request, "posts/index.html", {'projects': projects})

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProjectForm()
    return render(request, 'posts/create_project.html', {'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'posts/create_task.html', {'form': form})

