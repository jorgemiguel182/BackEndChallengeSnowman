# Generated by Django 3.0.8 on 2020-07-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200728_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbcategory',
            name='name',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]