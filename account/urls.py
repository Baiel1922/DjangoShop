from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('profile', ProfileViewset)

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('forgot-password-complete/', ForgotPasswordCompleteView.as_view()),
    path('', include(router.urls))
]