# Generated by Django 3.0.8 on 2020-07-22 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tbcategory',
            table='TB_CATEGORY',
        ),
        migrations.AlterModelTable(
            name='tbpicture',
            table='TB_PICTURE',
        ),
        migrations.AlterModelTable(
            name='tbtouristspot',
            table='TB_TOURIST_SPOT',
        ),
        migrations.AlterModelTable(
            name='tbuserfavorite',
            table='TB_USER_FAVORITE',
        ),
    ]
