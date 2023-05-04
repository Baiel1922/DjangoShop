from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics

from .serializers import ProductSerializer, BrandSerializer, SeasonSerializer, \
    GenderSerializer, CategorySerializer, ColorSerializer, SizeSerializer
from .models import Product, Brand, Season, Gender, Category, Color, Size
from .service import StandartResultsSetPagination


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny, ]

class SeasonListView(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [AllowAny, ]

class GenderListView(generics.ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [AllowAny, ]

class ColorListView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [AllowAny, ]

class SizeListView(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [AllowAny, ]


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAdminOrReadOnly, )
    pagination_class = StandartResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['category', 'brand', 'gender', 'season', 'price', 'in_stock']
    ordering_fields = '__all__'
