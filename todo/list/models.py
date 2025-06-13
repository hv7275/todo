from django.db import models
from django.utils import timezone

class Task(models.Model):
  
  CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Peronal', 'Personal'),
    ('Ohter', 'Other'),
  ]
  
  
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=timezone.now)
  category = models.CharField(max_length=8, choices=CATEGORY_CHOICES, default='Work')
  
  def __str__(self):
    return self.title
  


  

