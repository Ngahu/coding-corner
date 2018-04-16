from django.db import models

# Create your models here.



class List(models.Model):
    """
    will hold a single todo list
    """
    title =  models.CharField(maxlength=250, unique=True) 


    def __str__(self):
        return self.title