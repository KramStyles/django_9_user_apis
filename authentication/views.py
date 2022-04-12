from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
