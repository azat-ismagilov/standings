# Generated by Django 2.2.6 on 2019-11-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkoshp', '0004_auto_20191101_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
