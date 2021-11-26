from django.db import models

# Create your models here.
class Project(models.Model):
  title=models.CharField(max_length=100)
  intro=models.CharField(max_length=100, blank=True, default='Blank')
  image=models.ImageField(upload_to='project_photos/')
  description=models.TextField()
  link=models.URLField()
  githublink=models.URLField(blank=True, default='Blank')
  techUsed=models.CharField(max_length=500, blank=True, default='Tech used')