from posixpath import isabs
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
