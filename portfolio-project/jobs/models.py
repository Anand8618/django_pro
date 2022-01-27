from distutils.command import upload
from django.db import models
from prometheus_client import Summary
from sklearn.feature_extraction import image

# Create your models here.
class Job(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary