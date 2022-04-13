from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import permissions, exceptions
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer, LoginSerializer
from .models import User


class AuthUserApiView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)

        return Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    # Prevents authentication on this page
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginAPIView(GenericAPIView):
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        if not request.data.get('email'):
            raise exceptions.NotAcceptable('Email is Missing!')

        if not request.data.get('password'):
            raise exceptions.NotAcceptable('Password is required!')

        email = request.data['email']
        password = request.data['password']

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            resp = Response(serializer.data, status=204)
            resp.set_cookie(key='jwt', value=serializer.data['token'], httponly=True)
            return resp

        return Response({'message': 'Invalid Credentials. Try again'}, status=404)
