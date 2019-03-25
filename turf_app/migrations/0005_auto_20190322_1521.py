# Generated by Django 2.1.7 on 2019-03-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0004_fertiliserinuse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='address',
        ),
        migrations.AddField(
            model_name='distributor',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
    ]