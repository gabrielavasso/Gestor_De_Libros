from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor, Clasificacion
from .forms import LibroForm
from django.http import JsonResponse
import pandas as pd
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt  # ✅ Para pruebas desde Postman

def listar_libros(request):
    query = request.GET.get("q")
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros, 'query': query})

@csrf_exempt  # ✅ Solo para pruebas desde Postman
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def ver_pdf(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'libros/ver_pdf.html', {'libro': libro})

def recomendaciones(request):
    generos = Clasificacion.objects.all()
    sugerencias = []
    for genero in generos:
        libros = Libro.objects.filter(clasificacion=genero).order_by('?')[:2]
        sugerencias.append({
            'genero': genero.nombre,
            'libros': libros
        })

    # Leer valoraciones.csv y obtener libro con mayor puntaje
    ruta = os.path.join(settings.MEDIA_ROOT, 'valoraciones.csv')
    libro_mayor = None
    if os.path.exists(ruta):
        df = pd.read_csv(ruta)
        promedio_por_libro = df.groupby('libro')['valoracion'].mean().sort_values(ascending=False)
        if not promedio_por_libro.empty:
            titulo_mayor = promedio_por_libro.index[0]
            libro_mayor = Libro.objects.filter(titulo__icontains=titulo_mayor).first()

    return render(request, 'libros/recomendaciones.html', {
        'sugerencias': sugerencias,
        'libro': libro_mayor
    })

def api_libros(request):
    libros = Libro.objects.all()
    data = [{
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor.nombre,
        'clasificacion': libro.clasificacion.nombre,
        'pdf': libro.pdf.url if libro.pdf else None
    } for libro in libros]
    return JsonResponse(data, safe=False)

def api_libro_detalle(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    data = {
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor.nombre,
        'clasificacion': libro.clasificacion.nombre,
        'pdf': libro.pdf.url if libro.pdf else None
    }
    return JsonResponse(data)

def valoraciones(request):
    ruta = os.path.join(settings.MEDIA_ROOT, 'valoraciones.csv')
    if os.path.exists(ruta):
        df = pd.read_csv(ruta)
        media_por_genero = df.groupby('genero')['valoracion'].mean().reset_index()
        total_por_libro = df.groupby('libro')['valoracion'].count().reset_index()
        media_por_genero.columns = ['Género', 'Valoración Promedio']
        total_por_libro.columns = ['Libro', 'Cantidad de Valoraciones']
    else:
        media_por_genero = pd.DataFrame()
        total_por_libro = pd.DataFrame()
    return render(request, 'libros/valoraciones.html', {
        'media_por_genero': media_por_genero.to_dict(orient='records'),
        'total_por_libro': total_por_libro.to_dict(orient='records')
    })

def graficos(request):
    ruta = os.path.join(settings.MEDIA_ROOT, 'valoraciones.csv')
    grafico1 = {}
    grafico2 = {}
    if os.path.exists(ruta):
        df = pd.read_csv(ruta)
        grafico1 = df.groupby('genero')['valoracion'].mean().to_dict()
        grafico2 = df['libro'].value_counts().to_dict()
    return render(request, 'libros/graficos.html', {
        'grafico1': grafico1,
        'grafico2': grafico2
    })
