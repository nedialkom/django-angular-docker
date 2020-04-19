from django.contrib import admin
from django.urls import path

from todoapi import views as todoapi_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/', todoapi_views.TaskList.as_view(), name='task-list'),
    path('api/task/<int:task_id>/', todoapi_views.TaskDetail.as_view(), name='task-detail'),
]