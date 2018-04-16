from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL 
from django.db.models.signals import pre_save,post_save
from  .utils import unique_slug_generator




class TodoCategory(models.Model):
    """
    will hold a single todo list
    """
    owner = models.ForeignKey(User)
    title =  models.CharField(max_length=250, unique=True) 
    slug = models.SlugField(unique=True,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title


    
    class Meta:
         ordering = ['title'] 


def todo_category_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(todo_category_pre_save_receiver,sender=TodoCategory)



PRIORITY_CHOICES = ( 
  (0, 'Low'), 
  (1, 'Normal'), 
  (2, 'High'), 
)



class Todo(models.Model):
    """
    will hold a single to do item 
    eg  finish device registration
    """
    owner = models.ForeignKey(User)
    todo_list = models.ForeignKey(TodoCategory)
    title = models.CharField(max_length=250) 
    text = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1) 
    completed = models.BooleanField(default=False) 
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True,blank=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority', 'title'] 




def item_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(item_pre_save_receiver,sender=Todo)