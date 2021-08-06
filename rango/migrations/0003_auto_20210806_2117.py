# Generated by Django 2.1.5 on 2021-08-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210806_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='clothname',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(max_length=2560),
        ),
    ]