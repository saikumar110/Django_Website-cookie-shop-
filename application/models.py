from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)


class Orders(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.CharField(max_length=255)
    date = models.DateTimeField()
    time = models.CharField(max_length=200)


class posts(models.Model):
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=350)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
