# Generated by Django 4.2 on 2023-05-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combate',
            name='resultado',
            field=models.CharField(choices=[('Rojo', 'Rojo'), ('Empate', 'Empate'), ('Azul', 'Azul')]),
        ),
    ]
