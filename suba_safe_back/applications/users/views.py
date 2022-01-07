# Third Party Apps
from rest_framework.generics import (
    ListAPIView,
)

from firebase_admin import auth

from django.shortcuts import render

from django.views.generic import TemplateView

# Imports de DRF
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Imports de Serializadores
from .serializers import LoginSocialSerializer

# Modelos
from .models import User

from .serializers import UserSerializer


class LoginUser(TemplateView):
    template_name = 'users/login.html'


class GoogleLoginAPIView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        #Extraer token de la petición Web
        serializer = self.serializer_class(data=request.data)

        # Validar token
        serializer.is_valid(raise_exception=True)

        # Si el token es válido, entonces se extrae el id
        token = serializer.data.get('token_id')

        decoded_token = auth.verify_id_token(token)

        print('************************')
        print(decoded_token)
        print('************************')

        username = decoded_token['name']
        email = decoded_token['email']
        email_verified = decoded_token['email_verified']

        user, created = User.user_objects.get_or_create(
            email = email,
            defaults={
                'username': username,
                'email': email,
                'is_active': email_verified,
            }
        )

        if created:
            token = Token.objects.create(user=user)
        else:
            token = Token.objects.get(user=user)

        user_get = {
            'id': user.pk,
            'email': user.email,
            'username': user.username,
            'gender': user.gender,
            'phone': user.phone,
            'city': user.city,
        }

        return Response(
            {
                'token': token.key,
                'user': user_get,
            }
        )

class UserAPIView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.user_objects.all()