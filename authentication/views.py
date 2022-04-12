from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer, LoginSerializer
from .models import User


class AuthUserApiView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)

        return Response({'user': serializer.data}, status=203)


class RegisterAPIView(GenericAPIView):
    # queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=204)
        return Response({'message': 'Invalid Credentials. Try again'}, status=404)
