# Generated by Django 5.0.6 on 2024-10-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fristapp', '0002_rename_address_studentmodel_submission_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='submission_time',
            field=models.CharField(max_length=20),
        ),
    ]