# Generated by Django 5.0.3 on 2024-03-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0004_alter_voter_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='fname',
            field=models.CharField(default='Doe', max_length=100),
        ),
    ]
