import os
import geocoder
from decouple import config
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
    name = models.CharField(max_length=400, unique=True)
    
    class Meta:
        db_table = 'TB_CATEGORY'
        
    def __str__(self):
        return self.name
    

class TbUserFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE)
    tourist_spot = models.ForeignKey('TbTouristSpot', models.CASCADE)
    
    class Meta:
        db_table = 'TB_USER_FAVORITE'
        unique_together = ['user', 'tourist_spot']

    def __str__(self):
        return str(self.user.id)
    
    
class TbTouristSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400, unique=True)
    category = models.ForeignKey(TbCategory, models.DO_NOTHING)
    address = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    lat = models.CharField(max_length=50, null=True, blank=False)
    long = models.CharField(max_length=50, null=True, blank=False)

    class Meta:
        db_table = 'TB_TOURIST_SPOT'
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        api_key = os.environ.get("API_KEY_GOOGLE_MAPS", config('GOOGLE_MAPS_KEY', None))
        if (not self.lat and not self.long) and (self.address and self.state and self.country and api_key):
            v_address = str(self.address) + ', ' + str(self.state) + ', ' + str(self.country)
            g = geocoder.google(v_address, key=api_key)
            if g.json:
                self.lat = g.json['lat']
                self.long = g.json['lng']
        super(TbTouristSpot, self).save(*args, **kwargs)
