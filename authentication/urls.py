from django.urls import path

from authentication import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('user/', views.AuthUserApiView.as_view(), name='user'),
]
