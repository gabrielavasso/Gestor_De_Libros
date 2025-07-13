from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_libros, name='inicio'),  # Página principal con libros
    path('libros/crear/', views.crear_libro, name='crear_libro'),  # Crear libro
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),  # Página de recomendaciones
    path('api/libros/', views.api_libros, name='api_libros'),  # API de todos los libros
    path('api/libros/<int:libro_id>/', views.api_libro_detalle, name='api_libro_detalle'),  # API de detalle
    path('valoraciones/', views.valoraciones, name='valoraciones'),  # Vista con Pandas
    path('graficos/', views.graficos, name='graficos'),  # Gráficos
]
