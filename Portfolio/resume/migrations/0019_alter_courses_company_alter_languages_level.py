# Generated by Django 4.2.2 on 2023-08-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_courses_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='company',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='languages',
            name='level',
            field=models.CharField(max_length=20),
        ),
    ]