from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateTodoAPIView.as_view(), name='create-todo'),
    path('list/', views.TodoListAPIView.as_view(), name='list-todo'),
]
