from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogInView

urlpatterns= [
    path('login/', CustomLogInView.as_view(), name='login' ),
    path('', TaskList.as_view(), name='tasks' ),
    path('task/<int:pk>', TaskDetail.as_view(), name='task' ),
    path('create-task/', TaskCreate.as_view(), name='task-create' ),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update' ),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete' ),
]