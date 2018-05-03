from django.db import models


# Create your models here.

class PathRule(models.Model):
    path = models.CharField(max_length=100)
    rv = models.CharField(max_length=500)
    content_type = models.CharField(max_length=50, default='application/json')
