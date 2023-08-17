from django.db import models

# Create your models here.
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField()

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    youtube_link = models.URLField()
    description = models.TextField()
    images = models.ManyToManyField(GalleryImage, related_name='sermons')