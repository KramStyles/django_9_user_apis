from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer
from .models import Todo
# from todos import serializers


class ListCreateTodoApi(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'title', 'is_finished', 'desc']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TodoListAPIView(ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
