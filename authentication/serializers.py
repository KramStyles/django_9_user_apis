from rest_framework import serializers

from authentication.models import User


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=200, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
