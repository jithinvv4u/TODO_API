from django.db import models

# Create your models here.

class ToDo(models.Model):
    title=models.CharField(max_length=45)
    description=models.CharField(max_length=45,null=True)
    completed=models.BooleanField(default=0,null=True)
    created_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)