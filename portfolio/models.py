from os import link
from django.db import models

# Create your models here.
class Project(models.Model):
  title=models.CharField()
  image=models.ImageField(upload_to='project_photos/')
  description=models.TextField()
  link=models.URLField()