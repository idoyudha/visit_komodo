# Generated by Django 3.1.5 on 2021-03-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit_komodo', '0023_auto_20210328_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='CS50 Web Final Project'),
        ),
    ]
