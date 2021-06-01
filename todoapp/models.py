from django.db import models
from django.db.models.base import Model

# Create your models here.
class ToDoWork(models.Model):
    msg = models.CharField(max_length=200,blank=True)

class ToDoProject(models.Model):
    msg = models.CharField(max_length=200,blank=True)

class ToDoHobby(models.Model):
    msg = models.CharField(max_length=200,blank=True)