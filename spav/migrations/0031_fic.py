# Generated by Django 4.1 on 2022-09-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0030_faculty2_commitee'),
    ]

    operations = [
        migrations.CreateModel(
            name='FIC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('responsibility', models.CharField(choices=[('Grievance Cell', 'Grievance Cell'), ('Sexual Harassment of Women at workplace', 'Sexual Harassment of Women at workplace'), ('Art Lab', 'Art Lab'), ('Climatology/Energy Studies/Acoustic Lab', 'Climatology/Energy Studies/Acoustic Lab'), ('Structures lab/Material Testing Lab & Survey Lab', 'Structures lab/Material Testing Lab & Survey Lab'), ('Conservation Lab', 'Conservation Lab'), ('Landscape Lab', 'Landscape Lab'), ('Material and Construction Lab', 'Material and Construction Lab'), ('Computer Labs (Architecture , GIS )', 'Computer Labs (Architecture , GIS )'), ('Construction Yard', 'Construction Yard'), ('Model Making and Carpentry Workshop', 'Model Making and Carpentry Workshop'), ('Transportation Lab', 'Transportation Lab'), ('Environmental Lab', 'Environmental Lab'), ('Cultural Committee Head', 'Cultural Committee Head'), ('Nodal Office, Student Scholarships', 'Nodal Office, Student Scholarships')], max_length=50)),
                ('email', models.EmailField(default='cv', max_length=254)),
                ('phone', models.CharField(default=True, max_length=14)),
                ('date', models.DateField()),
                ('duties', models.TextField(default='Duties and Responsibilities of Deans')),
            ],
        ),
    ]