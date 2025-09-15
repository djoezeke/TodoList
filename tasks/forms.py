from django import forms

# models
from .models import List, Task


# List Form
class ListForm(forms.ModelForm):
    """Form for creating and updating a List."""

    title = forms.CharField(
        max_length=150,
        # widget=forms.TextInput(
        #     attrs={"class": "form-control", "placeholder": "List Title"}
        # ),
        # help_text="Enter a unique title for your list.",
    )
    description = forms.CharField(
        required=False,
        # widget=forms.Textarea(
        #     attrs={"class": "form-control", "placeholder": "Description", "rows": 3}
        # ),
        # help_text="Describe your list (optional).",
    )

    class Meta:
        """Meta options for the ListForm."""

        model = List
        fields = ["title", "description"]


class TaskForm(forms.ModelForm):
    """Form for creating and updating a Task."""

    title = forms.CharField(
        # max_length=150,
        # widget=forms.TextInput(
        #     attrs={"class": "form-control", "placeholder": "Task Title"}
        # ),
        # help_text="Enter the task title.",
    )
    description = forms.CharField(
        # required=False,
        # widget=forms.Textarea(
        #     attrs={"class": "form-control", "placeholder": "Description", "rows": 3}
        # ),
        # help_text="Describe the task (optional).",
    )
    completed = forms.BooleanField(
        # required=False,
        # widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        # help_text="Mark as completed.",
    )

    class Meta:
        """Meta options for the TaskForm."""

        model = Task
        fields = ["title", "description", "completed"]
