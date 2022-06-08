from django.db import models

class ReportPost(models.Model):
    """This class will initialize a report post model"""
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    reason = models.CharField(max_length=500)