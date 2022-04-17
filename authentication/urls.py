from django.urls import path

from authentication import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('user/', views.AuthUserApiView.as_view(), name='user'),
    path('verify/', views.VerifyEmailApiView.as_view(), name='email-verify'),
    path('reset/', views.ResetPasswordAPIView.as_view(), name='reset'),
    path('reset_password/', views.ChangePasswordApiView.as_view(), name='reset-password'),
    path('reset_change_password/', views.SetNewPassword.as_view(), name='reset-change-password'),
]
