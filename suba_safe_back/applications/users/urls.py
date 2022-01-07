from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('api/google-login', views.GoogleLoginAPIView.as_view(), name='google-login'),
    path('api/usuarios', views.UserAPIView.as_view(), name='usuarios')
]