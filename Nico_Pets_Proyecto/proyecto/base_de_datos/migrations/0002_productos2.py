# Generated by Django 4.0.4 on 2022-06-30 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_de_datos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre2', models.CharField(max_length=300)),
                ('descripcion2', models.CharField(max_length=100)),
                ('stock2', models.CharField(max_length=300)),
                ('precio2', models.CharField(max_length=300)),
                ('imagen2', models.CharField(max_length=300)),
            ],
        ),
    ]