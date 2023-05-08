from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryListView, BrandListView, SeasonListView, \
    GenderListView, ColorListView, SizeListView, ProductViewset, FavoriteViewset


router = DefaultRouter()
router.register('product', ProductViewset)
router.register('favorite', FavoriteViewset)

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    path('brand-list/', BrandListView.as_view()),
    path('season-list/', SizeListView.as_view()),
    path('gender-list/', GenderListView.as_view()),
    path('color-list/', ColorListView.as_view()),
    path('size-list/', SizeListView.as_view()),
    path('', include(router.urls)),
]