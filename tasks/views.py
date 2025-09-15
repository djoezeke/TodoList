from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.views import View
from django.contrib import messages

# Create your views here.


from .models import List, Task
from .forms import ListForm, TaskForm


# Helper functions.
def get_list_by_id_or_title(taskID):
    """Helper to fetch List by id or title."""
    if isinstance(taskID, int) or (isinstance(taskID, str) and taskID.isdigit()):
        return get_object_or_404(List, id=int(taskID))
    return get_object_or_404(List, title=taskID)


def get_task_by_id_or_title(taskID):
    """Helper to fetch Task by id or title."""
    if isinstance(taskID, int) or (isinstance(taskID, str) and taskID.isdigit()):
        return get_object_or_404(Task, id=int(taskID))
    return get_object_or_404(Task, title=taskID)


# Hompage View
def home(self, request: HttpRequest, ListID=None):
    form = ListForm()
    context = {"form": form}
    return render(request, "task/home.html", context)


########################### List Views ###########################
class CreateList(View):
    """View to create a new List."""

    def get(self, request: HttpRequest, ListID=None):
        form = ListForm()
        context = {"form": form}
        return render(request, "task/addlist.html", context)

    def post(self, request: HttpRequest, ListID=None):
        form = ListForm(request.POST)
        if form.is_valid():
            list_obj = form.save()
            messages.success(request, "List created successfully.")
            return redirect("task:view_list", list_obj.id)
        context = {"form": form}
        return render(request, "task/addlist.html", context)


class ReadList(View):
    """View to display a List and its Tasks."""

    def get(self, request: HttpRequest, ListID: str | int):
        list_obj = get_list_by_id_or_title(ListID)
        tasks = list_obj.tasks.all()
        search = request.GET.get("search", "")
        completed = request.GET.get("completed")
        order_by = request.GET.get("order_by")

        if search:
            tasks = tasks.filter(title__icontains=search)
        if completed is not None:
            tasks = tasks.filter(completed=(completed.lower() == "true"))
        if order_by in ["title", "created"]:
            tasks = tasks.order_by(order_by)

        context = {
            "list": list_obj,
            "tasks": tasks,
            "search": search,
            "completed": completed,
        }
        return render(request, "task/viewlist.html", context)

    def post(self, request: HttpRequest, ListID: str | int):
        # For compatibility, just re-render the list
        return self.get(request, ListID)


class UpdateList(View):
    """View to update an existing List."""

    def get(self, request: HttpRequest, ListID: str | int):
        list_obj = get_list_by_id_or_title(ListID)
        form = ListForm(instance=list_obj)
        context = {"form": form, "list": list_obj}
        return render(request, "task/updatelist.html", context)

    def post(self, request: HttpRequest, ListID: str | int):
        list_obj = get_list_by_id_or_title(ListID)
        form = ListForm(request.POST, instance=list_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "List updated successfully.")
            return redirect("task:view_list", list_obj.id)
        context = {"form": form, "list": list_obj}
        return render(request, "task/updatelist.html", context)


def delete_list(request: HttpRequest, ListID: str | int):
    """View to delete a List."""
    list_obj = get_list_by_id_or_title(ListID)
    list_obj.delete()

    return redirect("task:home")


########################### Task Views ###########################


class CreateTask(View):
    """View to create a new Task."""

    def get(self, request: HttpRequest, taskID: str | int):
        list_obj = get_list_by_id_or_title(taskID)
        form = TaskForm()
        context = {"form": form, "list": list_obj}
        return render(request, "task/addtask.html", context)

    def post(self, request: HttpRequest, taskID: str | int):
        list_obj = get_list_by_id_or_title(taskID)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.list = list_obj
            task.save()
            messages.success(request, "Task created successfully.")
            return redirect("task:view_task", task.id)
        context = {"form": form, "list": list_obj}
        return render(request, "task/addtask.html", context)


class ReadTask(View):
    """View to display a Task."""

    def get(self, request: HttpRequest, taskID: str | int):
        task = get_task_by_id_or_title(taskID)
        context = {"task": task}
        return render(request, "task/viewtask.html", context)

    def post(self, request: HttpRequest, taskID: str | int):
        # Usually, POST is not needed for read-only views, but kept for compatibility
        return self.get(request, taskID)


class UpdateTask(View):
    """View to update an existing Task."""

    def get(self, request: HttpRequest, taskID: str | int):
        task = get_task_by_id_or_title(taskID)
        form = TaskForm(instance=task)
        context = {"form": form, "task": task}
        return render(request, "task/updatetask.html", context)

    def post(self, request: HttpRequest, taskID: str | int):
        task = get_task_by_id_or_title(taskID)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("task:view_task", task.id)
        context = {"form": form, "task": task}
        return render(request, "task/updatetask.html", context)


def delete_task(request: HttpRequest, taskID: str | int):
    """View to delete a Task."""
    task = get_task_by_id_or_title(taskID)
    task.delete()
    messages.success(request, "Task deleted successfully.")
    return redirect("task:home")
