# Generated by Django 3.1.5 on 2021-03-08 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visit_komodo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='CS50 Web Project 4 Network', max_length=280)),
                ('date_join', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('imageURL', models.URLField(blank=True, null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
