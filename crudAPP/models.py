from django.db import models

# Create your models here.

class WebUser(models.Model):

    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.userName

class DeleteUser(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.userName
