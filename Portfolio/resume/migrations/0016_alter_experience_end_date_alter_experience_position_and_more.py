# Generated by Django 4.2.2 on 2023-08-17 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_portfolioproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='position',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='summery',
            name='adress',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='summery',
            name='e_mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='summery',
            name='name_surname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='summery',
            name='phone_number',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='summery',
            name='short_cv',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='summery',
            name='title',
            field=models.TextField(max_length=30),
        ),
    ]
