# Generated by Django 4.2 on 2024-12-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_fecha_remove_direccion_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='codigopostal',
            field=models.IntegerField(default='0000'),
        ),
    ]