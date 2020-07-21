from django.contrib.auth.models import User
from django.db import models


class TbPicture(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.ImageField()
    tourist_spot = models.ForeignKey('TbTouristSpot', models.DO_NOTHING)


class TbCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class TbUserFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    tourist_spot = models.ForeignKey('TbTouristSpot', models.DO_NOTHING)
    
    
class TbTouristSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    picture = models.ForeignKey(TbPicture, models.DO_NOTHING)
    geo_location = models.CharField(max_length=100)
    category = models.ForeignKey(TbCategory, models.DO_NOTHING)
    
    def __str__(self):
        return self.name
