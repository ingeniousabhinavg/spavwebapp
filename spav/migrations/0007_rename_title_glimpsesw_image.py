# Generated by Django 4.1 on 2022-09-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0006_glimpsesw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glimpsesw',
            old_name='title',
            new_name='image',
        ),
    ]
