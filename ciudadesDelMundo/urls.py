from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ciudades.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # autenticacion para los usuarios admin
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
