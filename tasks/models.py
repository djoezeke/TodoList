from django.db import models

# Create your models here.


# List Model
class List(models.Model):
    """
    Model representing a list of tasks.
    """

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for the List model."""

        verbose_name = "List"
        verbose_name_plural = "Lists"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title}"


# Task Model
class Task(models.Model):
    """
    Model representing a single task.
    """

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        """Meta options for the Task model."""

        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} ({'Done' if self.completed else 'Pending'})"
