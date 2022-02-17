# Generated by Django 4.0.2 on 2022-02-16 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyphoto', '0002_alter_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='music',
            field=models.FileField(blank=True, upload_to='music/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])]),
        ),
    ]
