# Generated by Django 4.2.2 on 2023-10-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_alter_courses_company_alter_languages_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='summery',
            name='short_cv',
            field=models.CharField(max_length=500),
        ),
    ]
