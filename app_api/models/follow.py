from django.db import models

class Follow(models.Model):
    """This class will initialize a report post model"""
    follower = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="followed")
