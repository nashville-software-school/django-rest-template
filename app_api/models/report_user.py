from django.db import models

class ReportUser(models.Model):
    """This class will initialize a report post model"""
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    reason = models.CharField(max_length=500)