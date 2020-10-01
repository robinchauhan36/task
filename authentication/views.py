import datetime

from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet

from authentication.serializers import RegistrationSerializer, LoginSerializer


class RegisterView(APIView):
    """
    Signup view-set is used for signup process.
    """
    http_method_names = ('post',)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        """
        Signup a user to our portal with some required attributes such as email, password, first_name phone etc
        Note- Phone number should be number and email & phone should be unique.
        :param request: wsgi request
        :param args: allows for any number of optional positional arguments (parameters), which will be assigned to a
        tuple named args
        :param kwargs: allows for any number of optional keyword arguments (parameters), which will be in a dict
        named kwargs
        :return: success-message or error message
        """
        serializer = self.serializer_class(data=request.data)
        value = request.data
        if serializer.is_valid():
            if value['email'] == value['confirm email']:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)



class LoginView(APIView):
    """
    create:
    Login view is used for login process.
    """
    serializer_class = LoginSerializer
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        """
        If request come with a valid credential (email/username and password) then generate token for request otherwise
        error message
        :param request: wsgi request
        :param args: allows for any number of optional positional arguments (parameters), which will be assigned to a
        tuple named args
        :param kwargs: allows for any number of optional keyword arguments (parameters), which will be in a dict
         named kwargs
        :return: success or error
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user_obj = serializer.validated_data.get('user')
            user_obj.last_login = datetime.datetime.now()
            user_obj.save()
            return Response(status=status.HTTP_200_OK, data=user_obj)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    get:
    Logout view is used for application logout process.
    """
    http_method_names = ('get',)
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get(self, request, *args, **kwargs):
        """
        Logout user
        :param request: wsgi request
        :param args: argument list
        :param kwargs: keyword argument object
        :return: success message or error
        """
        self.request.user.logout()
        return Response(status=status.HTTP_200_OK)