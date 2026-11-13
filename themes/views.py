from django.shortcuts import render, redirect
from .models import Contact, Faculty
from django.contrib import messages
# Create your views here.
def index(request):
    faculty_data = {
            'faculties': Faculty.objects.all(),
        }
    return render(request, 'index.html', faculty_data)

def about(request):
    faculty_data = {
        'faculties': Faculty.objects.all(),
    }
    return render(request, 'about.html', faculty_data)

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            user_data = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            user_data.save()
            success_msg = 'Successfully Sent Message'
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = 'Something went wrong'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')



