# Generated by Django 4.1.3 on 2022-12-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AddField(
            model_name='city',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
