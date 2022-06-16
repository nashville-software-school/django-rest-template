from django.db import models

class Post(models.Model):
    """This class will initialize a Post model"""
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="posts")
    created_on = models.DateTimeField()

    @property
    def is_liked(self):
        return self.__is_liked

    @is_liked.setter
    def is_liked(self, value):
        self.__is_liked = value
        
    @property
    def is_my_post(self):
        return self.__is_my_post
    
    @is_my_post.setter
    def is_my_post(self, value):
        self.__is_my_post = value
