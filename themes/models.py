from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    image = models.ImageField(upload_to='faculty')
    name = models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    research_area = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name