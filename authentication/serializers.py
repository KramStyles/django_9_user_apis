from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import encoding, http
from rest_framework import serializers

from authentication.models import User


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

    def validate(self, attrs):
        try:
            email = attrs.get('email', '')
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                uidb = http.urlsafe_base64_encode(user.id)
                token = PasswordResetTokenGenerator().make_token(user)
            pass
        except Exception as err:
            pass
        return super().validate(attrs)
