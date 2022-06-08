from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """This class will initialize a profile model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.FileField()
    tags = models.ManyToManyField("Tag", related_name="profile")
    bio = models.CharField(max_length=250)
    liked_comments = models.ManyToManyField("Comment", related_name="profile")
    liked_posts = models.ManyToManyField("Post", related_name="profile")
