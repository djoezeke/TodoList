from django import forms

# models
from .models import List, Task


# --- Forms for To-Do List App ---


class ListForm(forms.ModelForm):
    """
    Form for creating and updating a List.
    Fields:
        title (str): The name of the list.
        description (str): Optional description.
    """

    class Meta:
        model = List
        fields = ["title", "description"]


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating a Task.
    Fields:
        title (str): Task title.
        description (str): Optional description.
        completed (bool): Completion status.
    """

    class Meta:
        model = Task
        fields = ["title", "description", "completed"]
