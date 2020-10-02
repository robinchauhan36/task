import re

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from authentication import constant
from authentication.models import User
from authentication.validation import VALIDATION


class RegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        required=True, min_length=constant.CHARACTER_SIZE['phone_min'],
        max_length=constant.CHARACTER_SIZE['phone_max'],
        error_messages=VALIDATION['phone']
    )
    email = serializers.EmailField(required=True, error_messages=VALIDATION['email'])
    confirm_password = serializers.CharField()
    confirm_email = serializers.SerializerMethodField()
    password = serializers.CharField(required=True)
    address = serializers.CharField(required=False, error_messages=VALIDATION['address'])

    def validate_email(self, data):
        """
        Validate user exists with given email
        :param value: email
        :return: email or error
        """
        if User.objects.filter(email=data.lower()).exists():
            raise serializers.ValidationError('Already registered email!')
        return data.lower()


    def validate_phone(self, data):
        """
        check phone is valid or not
        :param value: phone
        :return: value(last-name) if valid, otherwise return validation error
        """
        value = data.strip()
        if re.match(constant.NUMBER_ONLY, value):
            if User.objects.filter(phone=value).exists():
                raise serializers.ValidationError('phone number already registered')
            return value
        raise serializers.ValidationError(VALIDATION['phone']['invalid'])

    def validate_telephone(self, data):
        """
        check telephone is valid or not
        :param value: telephone
        :return: value(last-name) if valid, otherwise return validation error
        """
        value = data.strip()
        if re.match(constant.NUMBER_ONLY, value):
            if User.objects.filter(telephone=value).exists():
                raise serializers.ValidationError('telephone number already registered')
            return value
        raise serializers.ValidationError(VALIDATION['phone']['invalid'])

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    @staticmethod
    def get_confirm_email(self, data):
        if data.get['email'] != data.get['confirm_email']:
            raise serializers.ValidationError(" email not matched")
        return data

    class Meta(object):
        """
        Define fields for this serializer
        """
        model = User
        fields = ('category', 'first_name', 'last_name', 'phone', 'email', 'confirm_email', 'password',
                  'confirm_password', 'company_name', 'telephone', 'address', 'country', 'state', 'city', 'zip_code')


class LoginSerializer(serializers.ModelSerializer):
    """
    Validate data and provide token for resource access

    create: validate request data for user-instance for login
    Return user-instance object

    to_representation :
    Return modified serializer (add new keys-values required for processing, and those keys are not
    required for processing, remove from serializer data) data of auth-user-instance

    """
    email = serializers.EmailField(required=True, error_messages=VALIDATION['email'])
    password = serializers.CharField(required=True, error_messages=VALIDATION['password'])

    @staticmethod
    def validate_email(value):
        """
        :param value: email
        :return: email
        """
        return value.lower()

    def validate(self, attrs):
        """
        Validate password those associated with user(email)
        :param attrs: attrs
        :return: attrs or error_message
        """
        password = attrs.get("password")
        email = attrs.get("email")

        if not User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError('wrong username or password')

        user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
        attrs['user'] = user
        return attrs

    class Meta(object):
        """
        Define fields for this serializer
        """
        model = User
        fields = ('email', 'password')
