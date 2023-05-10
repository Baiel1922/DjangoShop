import json
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.http import JsonResponse, HttpResponse

from .serializers import *
from .models import User

class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = 'Check your email! Activation code was sent!'
            return Response(message, status=201)

class ActivationView(APIView):
    def get(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Your account successfully acitvated!', status=200)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully signed out!', status=200)

class ForgotPasswordView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Activation code was sent! Check your email!')

class ForgotPasswordCompleteView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response("Password successfully has been changed!")


class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user)
        return queryset

# class ProfileInfoView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def get(self, request):
#         user = request.user
#         data = {
#             'first_name': user.first_name,
#             'last_name': user.last_name
#         }
#         return JsonResponse(data)
#
#     def put(self, request):
#         data = request.data
#         serializer = ProfileInfoSerializer(data=data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             return Response(serializer.data)
#         else:
#             return Response('Something went wrong!')


