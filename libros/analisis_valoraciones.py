import pandas as pd
import matplotlib.pyplot as plt
import django
import os
import sys

# Configurar Django para acceder a los modelos
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor.settings')
django.setup()

from libros.models import Libro

# Leer el archivo CSV (debe estar en la carpeta 'libros')
df = pd.read_csv('libros/valoraciones.csv')

# Obtener libros de la base de datos
libros = Libro.objects.in_bulk()

# Mapear datos del libro al DataFrame
df['titulo'] = df['libro_id'].map(lambda id: libros[id].titulo if id in libros else 'Desconocido')
df['clasificacion'] = df['libro_id'].map(lambda id: libros[id].clasificacion.nombre if libros[id].clasificacion else 'Sin clasificación')
df['autor'] = df['libro_id'].map(lambda id: libros[id].autor.nombre if libros[id].autor else 'Sin autor')

# Gráfico 1: Promedio de valoraciones por clasificación
valoracion_clasif = df.groupby('clasificacion')['valoracion'].mean().sort_values(ascending=False)
valoracion_clasif.plot(kind='bar', title='Promedio de valoraciones por clasificación', color='skyblue')
plt.ylabel('Valoración promedio')
plt.tight_layout()
plt.savefig('grafico_clasificacion.png')
plt.close()

# Gráfico 2: Promedio de valoraciones por autor
valoracion_autor = df.groupby('autor')['valoracion'].mean().sort_values(ascending=False)
valoracion_autor.plot(kind='bar', title='Promedio de valoraciones por autor', color='orange')
plt.ylabel('Valoración promedio')
plt.tight_layout()
plt.savefig('grafico_autor.png')
plt.close()
