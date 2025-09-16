from django import forms

# models
from .models import List, Task


# --- Forms for To-Do List App ---


class ListForm(forms.ModelForm):
    """ """

    class Meta:
        model = List
        fields = ["title", "description"]


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating a Task.
    """

    class Meta:
        model = Task
        fields = ["title", "description", "priority", "completed", "due_date"]
