from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL 


class List(models.Model):
    """
    will hold a single todo list
    """
    owner = models.OneToOneField(User)
    title =  models.CharField(max_length=250, unique=True) 
    slug = models.SlugField(unique=True,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

    
    class Meta:
         ordering = ['title'] 




PRIORITY_CHOICES = ( 
  (0, 'Low'), 
  (1, 'Normal'), 
  (2, 'High'), 
)



class Item(models.Model):
    """
    will hold a single to do item 
    eg  finish device registration
    """
    owner = models.OneToOneField(User)
    slug = models.SlugField(unique=True,blank=True, null=True)
    title = models.CharField(max_length=250) 
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1) 
    completed = models.BooleanField(default=False) 
    todo_list = models.ForeignKey(List)


    def __str__(self):
        self.title
    
    class Meta:
        ordering = ['-priority', 'title'] 


