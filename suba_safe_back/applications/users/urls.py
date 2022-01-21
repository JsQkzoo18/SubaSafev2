from unicodedata import name
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    # Url que carga un HTML template para ingresar al registro con Google
    path('login/', views.LoginUser.as_view(), name='login'),

    # Url para la validación de un token Firebase y el registro del usuario
    path('api/google-login/', views.GoogleLoginAPIView.as_view(), name='google-login'),
    # Url para registrar un usuario desde la aplicación interna
    path('api/auth/register/', views.RegisterAPIView.as_view(), name='auth-registrar'),
    # Url para receptar el token enviado por correo electrónico
    path('api/verificar-email/', views.VerifyEmail.as_view(), name='verificar-email'),
    # Url para iniciar sesión en una cuenta activada
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Url para la obtención de los datos personales
    path('api/auth/me/', views.UserAuthView.as_view(), name='auth-me'),
]