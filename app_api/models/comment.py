from django.db import models

class Comment(models.Model):
    """This class will initialize a comment model"""
    text = models.CharField(max_length=5000)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    created_on = models.DateTimeField()
