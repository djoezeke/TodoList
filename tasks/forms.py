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

    completed = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "type": "checkbox",
            }
        ),
        required=False,
        initial=False,
    )
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"},
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["title", "description", "priority", "completed", "due_date"]
