from django.db import models

# Create your models here.
class Episode(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()