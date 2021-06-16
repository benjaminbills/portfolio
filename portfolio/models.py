from django.db import models

# Create your models here.
class Project(models.Model):
  title=models.CharField(max_length=100)
  image=models.ImageField(upload_to='project_photos/')
  description=models.TextField()
  link=models.URLField()