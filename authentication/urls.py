from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication import views

urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    ]

