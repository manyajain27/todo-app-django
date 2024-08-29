from django.db import models

# Create your models here.
class Task(models.Model):
    heading=models.CharField(max_length=200)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    due=models.DateTimeField(null=True,blank=True)
    created=models.DateTimeField(null=True,blank=True)
    modified=models.DateTimeField(null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True)

    
    def __str__(self):
        return self.heading

class Category(models.Model):
    name=models.CharField(max_length=100)    
    def __str__(self):
        return self.name
    