from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static  # ✅ Importación necesaria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libros.urls')),  # Incluye las rutas de tu app "libros"
]

# ✅ Esto permite servir archivos estáticos y media en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])  # Corregido
