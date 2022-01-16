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
    # 
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Url para registrar un usuario desde la aplicación interna
    path('api/auth/register/', views.RegisterAPIView.as_view(), name='token_obtain_pair'),
    # Url para receptar el token enviado por correo electrónico
    path('verificar-email/', views.VerifyEmail.as_view(), name='verificar-email'),
]