from django.db import models

# --- Models for To-Do List App ---


class List(models.Model):
    """
    Model representing a list of tasks.
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
    """

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(
        default=0, choices=[(0, "Low"), (1, "Medium"), (2, "High")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["due_date", "priority"]

    def __str__(self):
        """String representation of the Task object."""
        return f"{self.title} ({'Done' if self.completed else 'Pending'})"
