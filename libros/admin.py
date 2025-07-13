from django.contrib import admin
from .models import Autor, Clasificacion, Libro

# Registro del modelo Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

# Registro del modelo Clasificacion
@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

# Registro del modelo Libro con PDF
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'clasificacion', 'pdf')
    list_filter = ('clasificacion',)
    search_fields = ('titulo', 'autor__nombre')
