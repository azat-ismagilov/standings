# Generated by Django 2.2.6 on 2019-10-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vkoshp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participant",
            name="codeforces_handle",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
    ]
