from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Achievement)
admin.site.register(First_Year)
admin.site.register(Second_Year)
admin.site.register(Third_Year)

class Sem1_list(admin.ModelAdmin):
    list_display = ('register_number', 'student_name', 'eng', 'maths', 'It', 'c_prog', 'social_media', 'word', 'word_lab', 'c_lab')
    
class Sem2_list(admin.ModelAdmin):
    list_display = ('register_number', 'student_name', 'eng', 'maths', 'animation', 'env_studies', 'computer_network', 'oops', 'oops_lab', 'animation_lab')
    
class Sem3_list(admin.ModelAdmin):
    list_display = ('register_number', 'student_name', 'sad', 'business_statics', 'computer_hardware', 'web_development', 'mis', 'os', 'hardware_lab', 'web_lab')
    
class Sem4_list(admin.ModelAdmin):
    list_display = ('register_number', 'student_name', 'python_prog', 'maths', 'php_framework', 'financial_accounting', 'database_admin', 'business_informatics', 'python_lab', 'php_lab')
    
class Sem5_list(admin.ModelAdmin):
    list_display = ('register_number', 'student_name', 'information_security', 'software_engineering', 'java', 'network_admin', 'digital_marketing', 'entrepreneurship_development', 'java_lab', 'major_project_phase1')
    
class Sem6_list(admin.ModelAdmin):
    list_display = ('register_number', 'student_name', 'hr_development', 'software_testing', 'It_society', 'advanced_java', 'mobile_application', 'foss', 'mobile_application_lab', 'major_project_phase2')

    
admin.site.register(Sem_1, Sem1_list)
admin.site.register(Sem_2, Sem2_list)
admin.site.register(Sem_3, Sem3_list)
admin.site.register(Sem_4, Sem4_list)
admin.site.register(Sem_5, Sem5_list)
admin.site.register(Sem_6, Sem6_list)