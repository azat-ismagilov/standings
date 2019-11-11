# Generated by Django 2.2.6 on 2019-10-31 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vkoshp', '0002_auto_20191028_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.CreateModel(
            name='HandleInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeforces_handle', models.CharField(blank=True, default='', max_length=50)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkoshp.Participant')),
            ],
        ),
    ]