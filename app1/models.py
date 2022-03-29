from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=100)
    Contact_No = models.CharField(max_length=15)
    Description = models.TextField()
    date = models.DateField()