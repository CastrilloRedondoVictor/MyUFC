# Generated by Django 4.2 on 2023-05-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luchadores', '0004_luchador_combates'),
    ]

    operations = [
        migrations.AddField(
            model_name='luchador',
            name='nacionalidad',
            field=models.CharField(blank=True, default='España', null=True),
        ),
        migrations.AlterField(
            model_name='luchador',
            name='guardia',
            field=models.CharField(choices=[('Diestra', 'Diestra'), ('Zurda', 'Zurda')]),
        ),
    ]