# Generated by Django 3.0.8 on 2020-07-23 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200722_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbtouristspot',
            name='pictures',
        ),
        migrations.AddField(
            model_name='tbpicture',
            name='tourist_spot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.TbTouristSpot'),
            preserve_default=False,
        ),
    ]
