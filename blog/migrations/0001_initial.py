# Generated by Django 3.2.6 on 2022-05-25 09:21

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evn1', models.CharField(choices=[('1', 'HIKING'), ('2', 'MOTOCR'), ('3', 'CAMPING')], help_text='Evento 1: ', max_length=10)),
                ('descripcion', models.CharField(help_text='Breve informacion', max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=blog.models.event_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del Hotel', max_length=20)),
                ('descripcion', models.CharField(help_text='Breve informacion', max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=blog.models.user_directory_path)),
                ('own', models.ForeignKey(help_text='Hotel admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Numero de habitacion')),
                ('capacity', models.CharField(blank=True, choices=[('1', '1Bed'), ('2', '2Bed'), ('4', '3Bed')], default='1', help_text='Numero de Camas', max_length=10)),
                ('descripcion', models.CharField(help_text='Breve informacion', max_length=100)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('custom', models.ManyToManyField(help_text='Nombre del huesped', to='blog.customer')),
                ('e1', models.ForeignKey(help_text='EVENTO 1', on_delete=django.db.models.deletion.CASCADE, to='blog.eventos')),
                ('resposable', models.ForeignKey(help_text='Hotel admin', on_delete=django.db.models.deletion.CASCADE, to='blog.hotel')),
            ],
        ),
        migrations.AddField(
            model_name='eventos',
            name='resp',
            field=models.ForeignKey(help_text='hotel : ', on_delete=django.db.models.deletion.CASCADE, to='blog.hotel'),
        ),
    ]
