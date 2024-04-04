from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Pharmmodels(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=15, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pharm_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return 'pharm_models'
    
    def get_absolute_url(self):
        return reverse("patients:uploadimage", args=[str(self.id)])
    
    



class PharmConverse(models.Model):
    Item = models.ForeignKey(Pharmmodels, on_delete=models.CASCADE)
    patient = models.ForeignKey(User ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'conversations'
    
class PharmMessages(models.Model):
    conversation = models.ForeignKey(PharmConverse, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return 'messages'