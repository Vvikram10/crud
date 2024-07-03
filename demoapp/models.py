# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=50)
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')
    address = models.TextField()

    def __str__(self):
        return self.name
