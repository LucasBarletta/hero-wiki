# Generated by Django 2.2.5 on 2019-09-30 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroi', '0004_auto_20190930_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroi',
            old_name='universo',
            new_name='universo_heroi',
        ),
    ]
