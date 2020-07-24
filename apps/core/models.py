from django.contrib.auth.models import User
from django.db import models


class TbPicture(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.ImageField()
    tourist_spot = models.ForeignKey('TbTouristSpot', models.CASCADE, related_name='pictures')
    
    class Meta:
        db_table = 'TB_PICTURE'

    def __str__(self):
        return self.picture.name


class TbCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    
    class Meta:
        db_table = 'TB_CATEGORY'
        
    def __str__(self):
        return self.name
    

class TbUserFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    tourist_spot = models.ForeignKey('TbTouristSpot', models.DO_NOTHING)
    
    class Meta:
        db_table = 'TB_USER_FAVORITE'
    
    
class TbTouristSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    geo_location = models.CharField(max_length=100)
    category = models.ForeignKey(TbCategory, models.DO_NOTHING)
    
    class Meta:
        db_table = 'TB_TOURIST_SPOT'
        
    def __str__(self):
        return self.name
