# Generated by Django 4.1 on 2022-09-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0013_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chairperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('designation', models.CharField(choices=[('Chairperson', 'Chairperson'), ('Chairperson in Charge ', 'Chairperson in Charge ')], max_length=50)),
                ('date', models.DateField()),
                ('profile_Pic', models.ImageField(max_length=254, upload_to='profiles')),
            ],
        ),
    ]
