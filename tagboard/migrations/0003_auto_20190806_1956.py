# Generated by Django 2.2.4 on 2019-08-06 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagboard', '0002_auto_20190806_1935'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='LocTags',
        ),
    ]
