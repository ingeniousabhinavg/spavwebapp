# Generated by Django 4.1 on 2022-09-08 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0016_bog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bog',
            name='profile_Pic',
        ),
    ]
