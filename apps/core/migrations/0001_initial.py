# Generated by Django 3.0.8 on 2020-07-22 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TbCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='TbPicture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TbTouristSpot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('geo_location', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.TbCategory')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.TbPicture')),
            ],
        ),
        migrations.CreateModel(
            name='TbUserFavorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tourist_spot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.TbTouristSpot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tbpicture',
            name='tourist_spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.TbTouristSpot'),
        ),
    ]
