# Generated by Django 4.0.1 on 2022-02-09 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyphoto', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picture',
            new_name='photo',
        ),
    ]
