# Generated by Django 4.2.2 on 2023-07-23 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0008_initials_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initials',
            name='user',
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
