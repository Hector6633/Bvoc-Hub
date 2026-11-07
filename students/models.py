from django.db import models

# Create your models here.
class Achievement(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    program_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class First_Year(models.Model):
    student_img = models.ImageField(upload_to='first-years/')
    name = models.CharField(max_length=20)
    candidate_code = models.BigIntegerField()
    def __str__(self):
        return self.name
    
class Second_Year(models.Model):
    student_img = models.ImageField(upload_to='second-years/')
    name = models.CharField(max_length=20)
    candidate_code = models.BigIntegerField()
    def __str__(self):
        return self.name
    
class Third_Year(models.Model):
    student_img = models.ImageField(upload_to='third-years/')
    name = models.CharField(max_length=20)
    candidate_code = models.BigIntegerField()
    def __str__(self):
        return self.name