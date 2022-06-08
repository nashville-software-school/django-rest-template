from django.db import models


class Music(models.Model):
    """This class will initialize a music model"""
    song = models.FileField()
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    genres = models.ManyToManyField("Genre", related_name="music")
