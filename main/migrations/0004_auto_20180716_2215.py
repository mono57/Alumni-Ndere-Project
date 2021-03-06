# Generated by Django 2.0.1 on 2018-07-16 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180712_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='createur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
