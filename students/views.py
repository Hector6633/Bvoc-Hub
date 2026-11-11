from django.shortcuts import render
from . models import First_Year, Second_Year, Third_Year, Achievement
# Create your views here.
def first_year(request):
    student_data = {
        'first_year': First_Year.objects.all(),
    }
    return render(request, 'first-year.html', student_data)

def second_year(request):
    student_data = {
            'second_year': Second_Year.objects.all(),
        }
    return render(request, 'second-year.html', student_data)

def third_year(request):
    student_data = {
            'third_year': Third_Year.objects.all(),
        }
    return render(request, 'third-year.html', student_data)

def achievements(request):
    achievements_data = {
            'achievements': Achievement.objects.all(),
        }
    return render(request, 'achievements.html', achievements_data)