# Generated by Django 5.0.6 on 2024-10-05 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fristapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='address',
            new_name='submission_time',
        ),
    ]