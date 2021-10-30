from django.urls import path 
from .views import Tasklist, taskdetail, TaskCreate,TaskUpdate,DeleteView,CustomLoginViews

urlpatterns=[
    path('login/',CustomLoginViews.as_view(),name='login'),
    path('',Tasklist.as_view(), name='tasks' ),
    path('task/<int:pk>/',taskdetail.as_view(), name='Task' ),
    path('task-create/',TaskCreate.as_view(), name='task-create' ),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update' ),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete' ),
] 