# Generated by Django 2.2.4 on 2019-08-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='id',
        ),
        migrations.AlterField(
            model_name='tags',
            name='tagname',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
