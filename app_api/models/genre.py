from django.db import models

class Genre(models.Model):
    """This class will initialize a genre model"""
    label = models.CharField(max_length=50)
