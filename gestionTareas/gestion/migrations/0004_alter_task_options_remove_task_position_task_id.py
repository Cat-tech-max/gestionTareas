# Generated by Django 5.0.6 on 2024-05-28 16:04

import gestion.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_remove_task_id_alter_task_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'description']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='position',
        ),
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=gestion.models.Task.generateUUID, editable=False, help_text='Valor unico por tarea', primary_key=True, serialize=False, unique=True),
        ),
    ]
