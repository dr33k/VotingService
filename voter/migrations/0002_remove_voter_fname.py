# Generated by Django 5.0.3 on 2024-03-26 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='fname',
        ),
    ]
