from django.db import models

class Post(models.Model):
    """This class will initialize a Post model"""
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    text = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_on = models.DateTimeField()

    @property
    def is_liked(self):
        return self._is_liked

    @is_liked.setter
    def is_liked(self, value):
        self._is_liked = value
