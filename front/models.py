from django.db import models
from django.utils import timezone

# Create your models here.

class Songs(models.Model):
    title = models.CharField('Name of the song',unique=True, max_length=50)
    date = models.DateTimeField('date', default=timezone.now)
    image = models.ImageField(upload_to="files")
    song = models.FileField(upload_to="files")

