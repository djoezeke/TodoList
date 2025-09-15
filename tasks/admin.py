from django.contrib import admin
from .models import List, Task


# Register your models here.


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    """ListAdmin"""

    list_display = ["title", "created"]
    search_fields = ["title"]
    date_hierarchy = "created"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """TaskAdmin"""

    list_display = ["title", "list"]
    search_fields = ["title", "list__title"]
    autocomplete_fields = ["list"]
