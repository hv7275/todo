from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
  
  CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Peronal', 'Personal'),
    ('Play', 'Play'),
    ('Sleep', 'Sleep'),
    ('Wake-Up-Time', 'Wake-Up'),
    ('Ohter', 'Other'),
  ]
  
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=timezone.now)
  category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, default='Work')

  
  def __str__(self):
    return self.title
  


  

