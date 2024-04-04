from django.db import models

# Create your models here.

class Boxes(models.Model):
    details = models.CharField(max_length=500)