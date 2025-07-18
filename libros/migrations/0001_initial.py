# Generated by Django 5.2.4 on 2025-07-09 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('embedding', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('archivo_pdf', models.FileField(blank=True, null=True, upload_to='libros_pdfs/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.autor')),
                ('clasificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='libros.clasificacion')),
            ],
        ),
    ]
