from random import randint

from django.conf import settings
from django.shortcuts import reverse
import jwt
from rest_framework import serializers, exceptions

from authentication.models import User
from .utils import Util


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=200, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')

        read_only_fields = ['token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'token')

        read_only_fields = ['token']


class MyResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

    def generate_otp(self):
        return randint(1000, 9999)

    def validate(self, attrs):
        try:
            email = attrs.get('email', '')
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)

                user.otp = self.generate_otp()
                user.save()

                token = user.token

                relative_link = reverse('reset-password')
                data = {
                    'subject': 'Reset Link',
                    'body': f"This is a message to reset your password. Your token is: {user.otp} and the link to click is: {settings.BASE_URL}{relative_link}?token={token} ",
                    'receiver': email
                }

                Util.send_email(data)


        except Exception as err:
            print('WAHALA', err)
            raise exceptions
        return super().validate(attrs)


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=1, max_length=100, write_only=True)
    token = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        fields = ['password', 'token']

    def validate(self, attrs):
        return super().validate(attrs)

class ValidateOTPSerializer(serializers.Serializer):
    otp = serializers.IntegerField()

    def validate(self, attrs):
        return super().validate(attrs)
