# Generated by Django 2.0.1 on 2018-08-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180801_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actualite',
            options={'ordering': ['-date_add']},
        ),
    ]
