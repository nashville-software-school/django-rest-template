from django.db import models


class Music(models.Model):
    """This class will initialize a music model"""
    title = models.CharField(max_length=30, default=None)
    song = models.FileField(upload_to='usermusic', max_length=None, null=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="songs")
    genres = models.ManyToManyField("Genre", related_name="music")
