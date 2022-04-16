from django.shortcuts import reverse
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import permissions, exceptions
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer, LoginSerializer, MyResetPasswordSerializer
from .models import User
from .utils import Util


class AuthUserApiView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)

        return Response({'user': serializer.data})


class VerifyEmailApiView(GenericAPIView):
    def get(self, request):
        pass


class RegisterAPIView(GenericAPIView):
    # Prevents authentication on this page
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        token = request.data['csrfmiddlewaretoken']

        relative_link = reverse('email-verify')
        if serializer.is_valid():

            data = {
                'subject': 'Registration Complete',
                'body': f"This is a Verification message. You have registered in <a href='{get_current_site(request).domain}{relative_link}{token}'>Homepage</a>. <br> Click to visit",
                'receiver': request.data['email']
            }
            # Util.send_email(data)
            serializer.save()
            print('TOKEN', serializer.data['token'])
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


class ResetPasswordAPIView(GenericAPIView):
    serializer_class = MyResetPasswordSerializer

    def post(self, request):
        pass
