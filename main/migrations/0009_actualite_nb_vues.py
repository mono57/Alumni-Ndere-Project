# Generated by Django 2.0.1 on 2018-07-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualite',
            name='nb_vues',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
