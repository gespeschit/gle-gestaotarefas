# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-04-01 13:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tarefas', '0002_tarefa'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefas.Categoria', verbose_name='Categoria'),
        ),
    ]
