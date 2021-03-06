# Generated by Django 3.1.5 on 2021-03-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit_komodo', '0019_auto_20210327_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_url',
            field=models.URLField(default='https://blog.airpaz.com/wp-content/uploads/Indonesia-1.jpg'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.CharField(default='Short description', max_length=100),
        ),
    ]
