# Generated by Django 4.0.4 on 2022-07-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_de_datos', '0002_productos2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=300)),
                ('nombres', models.CharField(max_length=300)),
                ('apellidoPaterno', models.CharField(max_length=300)),
                ('apellidoMaterno', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('teléfono', models.CharField(max_length=300)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
    ]