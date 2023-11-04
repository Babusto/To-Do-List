from django.urls import path
from .views import TaskList

urlpatterns= [
    path('', views.tasklist, name='tasks' )
]