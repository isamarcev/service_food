from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from service_food import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_service.urls')),
    path('api-auth/',
         include('rest_framework.urls',
                 namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

