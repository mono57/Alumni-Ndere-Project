# Generated by Django 2.0.1 on 2018-08-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20180818_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]