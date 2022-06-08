from django.db import models

class Comment(models.Model):
    """This class will initialize a comment model"""
    text = models.CharField(max_length=5000)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    created_on = models.DateTimeField()

    @property
    def is_liked(self):
        return self._is_liked

    @is_liked.setter
    def is_liked(self, value):
        self._is_liked = value
