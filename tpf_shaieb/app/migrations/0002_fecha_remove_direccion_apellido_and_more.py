# Generated by Django 4.2 on 2024-12-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='email',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='aaa@aaa.com', max_length=40),
        ),
        migrations.AddField(
            model_name='direccion',
            name='codigopostal',
            field=models.IntegerField(default='0000'),
        ),
    ]