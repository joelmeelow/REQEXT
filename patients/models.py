from django.db import models



class Boxes(models.Model):
    details = models.CharField(max_length=500)



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=400, default='stranger')
    email = models.CharField(max_length=200, default='ebuka@gmail.com')
    message = models.CharField(max_length=1000, default='nothing here')
