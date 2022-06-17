from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """This class will initialize a profile model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profileimages', height_field=None,
        width_field=None, max_length=None, null=True)
    tags = models.ManyToManyField("Tag", related_name="profile")
    bio = models.CharField(max_length=250)
    liked_comments = models.ManyToManyField("Comment", related_name="profiles")
    liked_posts = models.ManyToManyField("Post", related_name="profiles")
        
    @property
    def is_followed(self):
        return self.__is_following

    @is_followed.setter
    def is_following(self, value):
        self.__is_following = value
    
    @property
    def is_my_profile(self):
        return self.__is_my_profile

    @is_my_profile.setter
    def is_my_profile(self, value):
        self.__is_my_profile = value
