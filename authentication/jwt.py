from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication


class JWTAuthetication(BaseAuthentication):
    def authenticate(self, request):
        print('Request:', request)
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) != 2: raise exceptions.AuthenticationFailed('Invalid User Token')

        token = auth_token[1]
        return super().authenticate(request)
