# Generated by Django 4.2 on 2025-01-06 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_producto_categoria_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='direccion',
        ),
        migrations.DeleteModel(
            name='fecha',
        ),
    ]
