from django.urls import path, include
from .views import *

urlpatterns = [
    path('list/', CartItemView.as_view()),
    path('add/', CartItemAddView.as_view()),
    path('delete/<int:pk>/', CartItemDelView.as_view()),
    path('add_one/<int:pk>/', CartItemAddOneView.as_view()),
    path('reduce_one/<int:pk>/', CartItemReduceOneView.as_view()),
]