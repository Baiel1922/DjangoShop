from django.contrib import admin
from django.urls import path, include
from shop_root import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('account/', include('account.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += doc_urls