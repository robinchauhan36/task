from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.RegisterViewSet, basename='register')
router.register(r'login', views.LoginViewSet, basename='login')
router.register(r'logout', views.LogoutViewSet, basename='logout')

urlpatterns = router.urls

