# Generated by Django 5.0.3 on 2024-03-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0003_alter_voter_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='lname',
            field=models.CharField(max_length=100),
        ),
    ]
