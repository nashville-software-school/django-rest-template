from django.db import models

class Comment(models.Model):
    """This class will initialize a comment model"""
    text = models.CharField(max_length=5000)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    created_on = models.DateTimeField()

    @property
    def is_liked(self):
        return self.__is_liked

    @is_liked.setter
    def is_liked(self, value):
        self.__is_liked = value
    
    @property
    def is_my_comment(self):
        return self.__is_my_comment

    @is_my_comment.setter
    def is_my_comment(self, value):
        self.__is_my_comment = value
