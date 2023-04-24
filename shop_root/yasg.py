from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title='Shop API',
        default_version='v1',
        description='',
    ),
    public=True
)

urlpatterns = [path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), ]