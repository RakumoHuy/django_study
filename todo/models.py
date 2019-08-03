from django.db import models
from django import forms

# Create your models here.
PRIORITY_CHOICES=(('N','now'),('S','soon'),('L','late'))
class Category(models.Model):
    name = models.CharField(max_length = 200, unique = True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    datetime_created = models.DateTimeField(auto_now_add = True)
    is_finished = models.BooleanField(default = False)
    priority = models.CharField(max_length = 1, choices = PRIORITY_CHOICES, default = 'L')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
