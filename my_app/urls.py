from django.urls import path, include
from my_app.views import  SubTaskListCreateView, SubTaskDetailUpdateDeleteView, TaskListCreateView
from rest_framework.routers import DefaultRouter
from my_app.views import CategoryViewSet



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)


urlpatterns =[
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask_list_create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask_detail'),
    path('', include(router.urls)),
]

