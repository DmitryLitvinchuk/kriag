# Generated by Django 2.0.2 on 2018-04-29 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physical_properties', '0005_auto_20180429_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bpcg',
            old_name='component',
            new_name='substance',
        ),
    ]