import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import TemplateView
from rest_framework import status, viewsets
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from authentication.serializers import RegistrationSerializer, LoginSerializer


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class RegisterViewSet(viewsets.ModelViewSet):
    """
    Signup view-set is used for signup process.
    """
    http_method_names = ('post',)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Signup a user to our portal with some required attributes such as email, password, first_name phone etc
        Note- Phone number should be number and email & phone should be unique.
        :param request: wsgi request
        :return: success-message or error message
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return render(request, 'index.html', context)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class LoginViewSet(viewsets.ModelViewSet):
    """
    create:
    Login view is used for login process.
    """
    serializer_class = LoginSerializer
    http_method_names = ('post',)

    def post(self, request):
        """
        If request come with a valid credential (email/username and password) then generate token for request otherwise
        error message
        :param request: wsgi request
        :return: success or error
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user_obj = serializer.validated_data.get('user')
            user_obj.last_login = datetime.datetime.now()
            user_obj.save()
            return Response(status=status.HTTP_200_OK, data=user_obj)
        return Response(status=status.HTTP_400_BAD_REQUEST)



def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class LogoutViewSet(viewsets.ModelViewSet):
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
