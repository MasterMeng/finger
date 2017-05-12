from django.db import models

# Create your models here.

class Finger(models.Model):
    finger = models.CharField(max_length=20,null=True)
    os = models.CharField(max_length=20,null=True)
    os_ver = models.CharField(max_length=20,null=True)
    browser = models.CharField(max_length=20,null=True)
    browser_ver = models.CharField(max_length=20,null=True)
