from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.views import View
from django.contrib import messages

# Create your views here.


from .models import List, Task
from .forms import ListForm, TaskForm


# --- Helper functions ---
def get_list_by_id_or_title(listID):
    """
    Fetch List by id or title.
    Args:
        listID (int|str): List id or title.
    Returns:
        List instance.
    """
    if isinstance(listID, int) or (isinstance(listID, str) and listID.isdigit()):
        return get_object_or_404(List, id=int(listID))
    return get_object_or_404(List, title=listID)


def get_task_by_id_or_title(taskID):
    """
    Fetch Task by id or title.
    Args:
        taskID (int|str): Task id or title.
    Returns:
        Task instance.
    """
    if isinstance(taskID, int) or (isinstance(taskID, str) and taskID.isdigit()):
        return get_object_or_404(Task, id=int(taskID))
    return get_object_or_404(Task, title=taskID)


def home(request: HttpRequest):
    """
    Homepage view: shows form to create a new list.
    """
    ls = List.objects.prefetch_related("tasks").all()
    form = ListForm()
    context = {"form": form, "lists": ls}
    return render(request, "tasks/index.html", context)


def lists(request: HttpRequest):
    """
    View to display all lists (optimized with prefetch_related).
    """
    ls = List.objects.prefetch_related("tasks").all()
    context = {"lists": ls}
    return render(request, "tasks/alllist.html", context)


def tasks(request: HttpRequest):
    """
    View to display all tasks (optimized with select_related).
    """
    ts = Task.objects.select_related("list").all()
    context = {"tasks": ts}
    return render(request, "tasks/alltask.html", context)


def about(request: HttpRequest):
    """
    View to display about
    """
    context = {}
    return render(request, "tasks/about.html", context)


########################### List Views ###########################
class CreateList(View):
    """View to create a new List."""

    def get(self, request: HttpRequest, listID: str | int = None):
        form = ListForm()
        context = {"form": form}
        return render(request, "tasks/addlist.html", context)

    def post(self, request: HttpRequest, listID: str | int = None):
        form = ListForm(request.POST)
        if form.is_valid():
            list_obj = form.save()
            messages.success(request, "List created successfully.")
            return redirect("tasks:view_list", list_obj.id)
        context = {"form": form}
        return render(request, "tasks/addlist.html", context)


class ReadList(View):
    """View to display a List and its Tasks."""

    def get(self, request: HttpRequest, listID: str | int):
        """
        Display a List and its Tasks, with search/filter/order options.
        Optimized with prefetch_related.
        """
        list_obj = get_list_by_id_or_title(listID)
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
        return render(request, "tasks/viewlist.html", context)

    def post(self, request: HttpRequest, listID: str | int):
        # For compatibility, just re-render the list
        return self.get(request, listID)


class UpdateList(View):
    """View to update an existing List."""

    def get(self, request: HttpRequest, listID: str | int):
        list_obj = get_list_by_id_or_title(listID)
        form = ListForm(instance=list_obj)
        context = {"form": form, "list": list_obj}
        return render(request, "tasks/updatelist.html", context)

    def post(self, request: HttpRequest, listID: str | int):
        list_obj = get_list_by_id_or_title(listID)
        form = ListForm(request.POST, instance=list_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "List updated successfully.")
            return redirect("tasks:view_list", list_obj.id)
        context = {"form": form, "list": list_obj}
        return render(request, "tasks/updatelist.html", context)


def delete_list(request: HttpRequest, listID: str | int):
    """View to delete a List."""
    list_obj = get_list_by_id_or_title(listID)
    list_obj.delete()

    return redirect("tasks:home")


########################### Task Views ###########################


class CreateTask(View):
    """View to create a new Task."""

    def get(self, request: HttpRequest, listID: str | int):
        list_obj = get_list_by_id_or_title(listID)
        form = TaskForm()
        context = {"form": form, "list": list_obj}
        return render(request, "tasks/addtask.html", context)

    def post(self, request: HttpRequest, listID: str | int):
        list_obj = get_list_by_id_or_title(listID)
        form = TaskForm(request.POST)
        if form.is_valid():
            tasks = form.save(commit=False)
            tasks.list = list_obj
            tasks.save()
            messages.success(request, "Task created successfully.")
            return redirect("tasks:view_task", tasks.id)
        context = {"form": form, "list": list_obj}
        return render(request, "tasks/addtask.html", context)


class ReadTask(View):
    """View to display a Task."""

    def get(self, request: HttpRequest, taskID: str | int):
        """
        Display a single Task (optimized with select_related).
        """
        tasks = get_task_by_id_or_title(taskID)
        context = {"tasks": tasks}
        return render(request, "tasks/viewtask.html", context)

    def post(self, request: HttpRequest, taskID: str | int):
        # Usually, POST is not needed for read-only views, but kept for compatibility
        return self.get(request, taskID)


class UpdateTask(View):
    """View to update an existing Task."""

    def get(self, request: HttpRequest, taskID: str | int):
        tasks = get_task_by_id_or_title(taskID)
        form = TaskForm(instance=tasks)
        context = {"form": form, "tasks": tasks}
        return render(request, "tasks/updatetask.html", context)

    def post(self, request: HttpRequest, taskID: str | int):
        tasks = get_task_by_id_or_title(taskID)
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("tasks:view_task", tasks.id)
        context = {"form": form, "tasks": tasks}
        return render(request, "tasks/updatetask.html", context)


def delete_task(request: HttpRequest, taskID: str | int):
    """View to delete a Task."""
    tasks = get_task_by_id_or_title(taskID)
    tasks.delete()
    messages.success(request, "Task deleted successfully.")
    return redirect("tasks:home")
