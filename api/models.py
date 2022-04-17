from django.db import models

# Create your models here.

class Widget(models.Model):
  id = models.AutoField(primary_key=True,blank=True)
  widget = models.CharField(max_length=1000000,blank=True)
  function = models.CharField(max_length=1000000,blank=True)
      
  def __str__(self):
    return str(self.id)
  
