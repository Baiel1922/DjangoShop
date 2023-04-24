from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import ProductSerializer, BrandSerializer, SeasonSerializer, \
    GenderSerializer, CategorySerializer
from .models import Product, Brand, Season, Gender, Category


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )

class BrandViewset(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAdminOrReadOnly, )

class SeasonViewset(ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = (IsAdminOrReadOnly, )

class GenderViewset(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['category', 'brand', 'gender', 'season', 'price', 'in_stock']
    ordering_fields = '__all__'
