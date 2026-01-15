from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, RegisterForm
from .models import Task
from django.http import JsonResponse
from django.contrib import messages
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = RegisterForm()
    return render(request, "tasks/register.html", {"form": form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    form = TaskForm()
    return render(request, "tasks/task_list.html", {"tasks": tasks, "form": form})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    return redirect("task_list")

@login_required
def mark_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    return redirect("task_list")

@login_required
def toggle_complete_ajax(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_completed = not task.is_completed
        task.save()
        return JsonResponse({"success": True, "is_completed": task.is_completed})
    return JsonResponse({"success": False}, status=400)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("task_list")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "tasks/login.html", {"form": None})
    return render(request, "tasks/login.html", {"form": None})
