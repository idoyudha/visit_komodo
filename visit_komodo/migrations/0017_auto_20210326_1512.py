# Generated by Django 3.1.5 on 2021-03-26 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit_komodo', '0016_auto_20210326_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_by',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='destination',
            old_name='created_by',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='created_by',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='created_by',
            new_name='author',
        ),
    ]