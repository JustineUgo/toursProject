from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Business(models.Model):
    
    name = models.CharField(max_length=100)
    
    pic = models.ImageField(upload_to="profile_pic", blank=True,)#change blank=False
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=50) #change to standard address to enable rader
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    

class Wheel(models.Model):
    
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(Business, on_delete=models.SET_NULL, related_name='business_wheel_set', null=True)
    members = models.ManyToManyField(Business)

    def __str__(self):
        return self.name



class Endorsement(models.Model):
    
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_endorsements_set')
    endorsers = models.ManyToManyField(Business, related_name='endorsers', blank=True)
    endorses = models.ManyToManyField(Business, related_name='endorses', blank=True)
    
    def __str__(self):
        return str(self.business)
    


class Media(models.Model):
    
    title = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="music/cover", blank=True,)
    date = models.DateTimeField(auto_now=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_media_set')
    music= models.FileField(upload_to = 'music/%Y/%m/%d', default=True)    
    played = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title



class ShelfPhoto(models.Model):
    
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='shelfphotos/%Y/%m/%d', blank=False)
    price = models.CharField(max_length=70)
    #shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name = 'shelf_shelfphoto_set')
    is_published = models.BooleanField(default=True)
    is_ad = models.BooleanField(default = False)
    

    def __str__(self):
        return self.name



class Shelf(models.Model):
    
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_shelf_set')
    is_published = models.BooleanField(default = True)
    photos = models.ManyToManyField(ShelfPhoto, blank=True)
    
    def __str__(self):
        return str((self.created_by.name) + '-' + self.name)

    








