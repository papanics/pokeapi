from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include ('api.urls')),
    path('', include ('pokemon_app.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)