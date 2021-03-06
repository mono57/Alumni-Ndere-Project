# Generated by Django 2.0.1 on 2018-08-07 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0008_remove_appartenir_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateTimeField(auto_now=True)),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Groupe')),
            ],
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['-date_add']},
        ),
        migrations.RenameField(
            model_name='appartenir',
            old_name='groupe',
            new_name='group',
        ),
    ]
