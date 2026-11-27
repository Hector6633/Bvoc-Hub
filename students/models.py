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
    
class Sem_1(models.Model):
    register_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    eng = models.IntegerField()
    maths = models.IntegerField()
    It = models.IntegerField()
    c_prog = models.IntegerField()
    word = models.IntegerField()
    social_media = models.IntegerField()
    word_lab = models.IntegerField()
    c_lab = models.IntegerField()
    cgpa = models.FloatField()
    
    def __str__(self):
        return self.student_name
    
class Sem_2(models.Model):
    register_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    eng = models.IntegerField()
    maths = models.IntegerField()
    animation = models.IntegerField()
    env_studies = models.IntegerField()
    computer_network = models.IntegerField()
    oops = models.IntegerField()
    oops_lab = models.IntegerField()
    animation_lab = models.IntegerField()
    cgpa = models.FloatField()
    
    def __str__(self):
        return self.student_name
    
class Sem_3(models.Model):
    register_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    business_statics = models.IntegerField()
    web_development = models.IntegerField()
    computer_hardware = models.IntegerField()
    sad = models.IntegerField()
    mis = models.IntegerField()
    os = models.IntegerField()
    hardware_lab = models.IntegerField()
    web_lab = models.IntegerField()
    cgpa = models.FloatField()
    
    def __str__(self):
        return self.student_name
    
class Sem_4(models.Model):
    register_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    python_prog = models.IntegerField()
    maths = models.IntegerField()
    php_framework = models.IntegerField()
    financial_accounting = models.IntegerField()
    database_admin = models.IntegerField()
    business_informatics = models.IntegerField()
    python_lab = models.IntegerField()
    php_lab = models.IntegerField()
    cgpa = models.FloatField()
    
    def __str__(self):
        return self.student_name
    
class Sem_5(models.Model):
    register_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    information_security = models.IntegerField()
    software_engineering = models.IntegerField()
    digital_marketing = models.IntegerField()
    network_admin = models.IntegerField()
    entrepreneurship_development = models.IntegerField()
    java = models.IntegerField()
    java_lab = models.IntegerField()
    major_project_phase1 = models.IntegerField()
    cgpa = models.FloatField()
    
    def __str__(self):
        return self.student_name
    
class Sem_6(models.Model):
    register_number = models.BigIntegerField()
    student_name = models.CharField(max_length=50)
    hr_development = models.IntegerField()
    It_society = models.IntegerField()
    advanced_java = models.IntegerField()
    foss = models.IntegerField()
    mobile_application = models.IntegerField()
    software_testing = models.IntegerField()
    mobile_application_lab = models.IntegerField()
    major_project_phase2 = models.IntegerField()
    cgpa = models.FloatField()
    
    def __str__(self):
        return self.student_name
    
    