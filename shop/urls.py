from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewset, BrandViewset, SeasonViewset, \
    GenderViewset, ProductViewset


router = DefaultRouter()
router.register('category', CategoryViewset)
router.register('brand', BrandViewset)
router.register('season', SeasonViewset)
router.register('gender', GenderViewset)
router.register('product', ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]