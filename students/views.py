from django.shortcuts import render
from . models import First_Year, Second_Year, Third_Year, Achievement
# Create your views here.
def first_year(request):
    student_data = {
        'first_year': First_Year.objects.all(),
    }
    return render(request, 'first-year.html', student_data)

def second_year(request):
    return render(request, 'second-year.html')

def third_year(request):
    return render(request, 'third-year.html')

def achievements(request):
    return render(request, 'achievements.html')