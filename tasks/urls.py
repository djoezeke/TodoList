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

from .views import home, tasks, lists, about

app_name: str = "tasks"

urlpatterns = [
    path("", home, name="home"),
    # User URLs
    path("add/", CreateList.as_view(), name="add_list"),
    path("tasks/", tasks, name="all_task"),
    path("lists/", lists, name="all_list"),
    path("about/", about, name="about"),
    # List URLs
    path("<int:listID>/", ReadList.as_view(), name="view_list"),
    path("<str:listID>/", ReadList.as_view(), name="view_list"),
    path("<int:listID>/update/", UpdateList.as_view(), name="update_list"),
    path("<str:listID>/update/", UpdateList.as_view(), name="update_list"),
    path("<int:listID>/delete/", delete_list, name="delete_list"),
    path("<str:listID>/delete/", delete_list, name="delete_list"),
    # Task URLs (nested under list)
    path("<int:listID>/add/", CreateTask.as_view(), name="add_task"),
    path("<str:listID>/add/", CreateTask.as_view(), name="add_task"),
    # Task URLs (by task id or title)
    path("task/<int:taskID>/", ReadTask.as_view(), name="view_task"),
    path("task/<str:taskID>/", ReadTask.as_view(), name="view_task"),
    path("task/<int:taskID>/update/", UpdateTask.as_view(), name="update_task"),
    path("task/<str:taskID>/update/", UpdateTask.as_view(), name="update_task"),
    path("task/<int:taskID>/delete/", delete_task, name="delete_task"),
    path("task/<str:taskID>/delete/", delete_task, name="delete_task"),
]
