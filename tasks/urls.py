"""
URL configuration for tasks.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    CreateList,
    ReadList,
    UpdateList,
    delete_list,
)

from .views import (
    CreateTask,
    ReadTask,
    UpdateTask,
    delete_task,
)

from .views import home

app_name: str = "task"

urlpatterns = [
    path("", home, name="home"),
    # User URLs
    path("add/", CreateList.as_view(), name="add_list"),
    # List URLs
    path("<int:ListID>/", ReadList.as_view(), name="view_list"),
    path("<str:ListID>/", ReadList.as_view(), name="view_list"),
    path("<int:ListID>/update/", UpdateList.as_view(), name="update_list"),
    path("<str:ListID>/update/", UpdateList.as_view(), name="update_list"),
    path("<int:ListID>/delete/", delete_list, name="delete_list"),
    path("<str:ListID>/delete/", delete_list, name="delete_list"),
    # Task URLs (nested under list)
    path("<int:ListID>/add/", CreateTask.as_view(), name="add_task"),
    path("<str:ListID>/add/", CreateTask.as_view(), name="add_task"),
    # Task URLs (by task id or title)
    path("task/<int:taskID>/", ReadTask.as_view(), name="view_task"),
    path("task/<str:taskID>/", ReadTask.as_view(), name="view_task"),
    path("task/<int:taskID>/update/", UpdateTask.as_view(), name="update_task"),
    path("task/<str:taskID>/update/", UpdateTask.as_view(), name="update_task"),
    path("task/<int:taskID>/delete/", delete_task, name="delete_task"),
    path("task/<str:taskID>/delete/", delete_task, name="delete_task"),
]
