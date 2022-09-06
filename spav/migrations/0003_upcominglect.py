# Generated by Django 4.1 on 2022-09-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0002_noticeboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingLect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lectureTitle', models.CharField(max_length=200)),
                ('lectureFile', models.FileField(upload_to='ulect')),
                ('lectureUrl', models.URLField(null=True)),
                ('lectureDate', models.DateField()),
            ],
        ),
    ]