from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import User, Profile

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirmation = serializers.CharField(required=True, min_length=6)

    def validate_email(self, email):
        if User.objects.filter(email=email, is_active=True).exists():
            raise serializers.ValidationError('Email is already taken')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self):
        attrs = self.validated_data
        user = User.objects.create_user(**attrs)
        code = user.generate_activation_code()
        user.send_activation_email(user.email, code)
        return user


class ActivationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    activation_code = serializers.CharField(min_length=6, max_length=6)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User is not found')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Activation code not found')
        return code


    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('activation_code')
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError('Activation code not found')
        return attrs

    def activate(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.activation_code = ''
        user.save()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email, is_active=True).exists():
            raise serializers.ValidationError('User not found!')
        return email

    def validate(self, attrs):
        request = self.context.get('request')
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(email=email, password=password, request=request)
            if not user:
                raise serializers.ValidationError('Incorrect email or password')

        else:
            raise serializers.ValidationError('Password and email required!')

        attrs['user'] = user
        return attrs

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User is not registrated!')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        code = user.generate_activation_code()
        user.send_activation_email(email, code)
        return email

class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirmation = serializers.CharField(required=True, min_length=6)
    code = serializers.CharField(required=True, min_length=6, max_length=6)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists:
            raise serializers.ValidationError('User is not registrated')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Activation code is not correct')
        return code

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.get('password_confirmation')
        if password_confirmation != password:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.activation_code = ''
        user.set_password(password)
        user.save()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# class ProfileSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=100, required=True)
#     last_name = serializers.CharField(max_length=100, required=True)
#     def validate(self, validated_data):
#         request = self.context.get('request')
#         user = request.user
#         user.first_name = validated_data.get('first_name')
#         user.last_name = validated_data.get('last_name')
#         user.save()
#         return validated_data



