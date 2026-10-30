from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

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

def achievements(request):
    return render(request, 'achievements.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')