# Generated by Django 3.1.5 on 2021-02-04 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210204_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='users',
            new_name='user',
        ),
    ]
