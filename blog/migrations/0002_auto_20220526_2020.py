# Generated by Django 3.2.6 on 2022-05-26 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='e2',
            field=models.ForeignKey(default='2', help_text='EVENTO 1', on_delete=django.db.models.deletion.CASCADE, related_name='E2', to='blog.eventos'),
        ),
        migrations.AlterField(
            model_name='room',
            name='e1',
            field=models.ForeignKey(default='1', help_text='EVENTO 1', on_delete=django.db.models.deletion.CASCADE, related_name='E1', to='blog.eventos'),
        ),
    ]