# Generated by Django 4.2 on 2023-05-03 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('luchadores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Combate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateField()),
                ('round_max', models.PositiveIntegerField()),
                ('resultado', models.CharField(choices=[('rojo', 'Rojo'), ('empate', 'Empate'), ('azul', 'Azul')])),
                ('golpes_rojo', models.PositiveIntegerField()),
                ('golpes_acertados_rojo', models.PositiveIntegerField()),
                ('golpes_fallados_rojo', models.PositiveIntegerField()),
                ('golpes_azul', models.PositiveIntegerField()),
                ('golpes_acertados_azul', models.PositiveIntegerField()),
                ('golpes_fallados_azul', models.PositiveIntegerField()),
                ('boxeador_azul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combates_azul', to='luchadores.luchador')),
                ('boxeador_rojo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combates_rojo', to='luchadores.luchador')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
