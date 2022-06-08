from django.db import models

class Tag(models.Model):
    """This class will initialize a tag model"""
    label = models.CharField(max_length=50)
