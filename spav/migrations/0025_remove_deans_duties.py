# Generated by Django 4.1 on 2022-09-09 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0024_alter_deans_duties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deans',
            name='duties',
        ),
    ]
