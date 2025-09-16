from django.db import models

# --- Models for To-Do List App ---


class List(models.Model):
    """
    Model representing a list of tasks.
    Fields:
        title (str): The name of the list (unique).
        description (str): Optional description.
        created (datetime): Timestamp when the list was created.
    """

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"
        ordering = ["-created"]

    def __str__(self):
        """String representation of the List object."""
        return self.title


class Task(models.Model):
    """
    Model representing a single task.
    Fields:
        list (List): ForeignKey to List.
        title (str): Task title.
        description (str): Optional description.
        created (datetime): Timestamp when the task was created.
        completed (bool): Completion status.
    """

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created"]

    def __str__(self):
        """String representation of the Task object."""
        return f"{self.title} ({'Done' if self.completed else 'Pending'})"
