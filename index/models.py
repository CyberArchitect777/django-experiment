from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Destination(models.Model):
    country = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    country_image = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.country


    
