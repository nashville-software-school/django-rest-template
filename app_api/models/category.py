from django.db import models

class Category(models.Model):
    """This class will initialize a category model"""
    label = models.CharField(max_length=120)
