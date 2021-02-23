from django.db import models

# Create your models here.

class unsplash_photos(models.Model):
    photo_id = models.CharField(max_length=11, primary_key=True, null=False, default=None)
    photo_url= models.CharField(max_length=255, null=True) 
    photo_image_url = models.CharField(max_length=255, null=True)
    photo_width = models.IntegerField(null=True)
    photo_height = models.IntegerField(null=True)
    photo_aspect_ratio = models.FloatField(null=True) 
    photo_description = models.CharField(max_length=5000, null=True)
    photographer_first_name  = models.CharField(max_length=255, null=True)
    photographer_last_name  = models.CharField(max_length=255, null=True)
    photo_location_country  = models.CharField(max_length=255, null=True)
    photo_location_city  = models.CharField(max_length=255, null=True)
    tagged = models.BooleanField(default=False)

    def __str__(self):
        return self.photo_id
