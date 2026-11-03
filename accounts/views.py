from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user_data = User.objects.create_user(username=username, email=email, password=password)
            user_data.save()
            success_msg = 'Successfully Signed Up'
            messages.success(request, success_msg)
            return redirect('sign_in')
        except Exception as e:
            error_msg = 'Username already exists'
            messages.error(request, error_msg)
            return redirect('sign_up')
    return render(request, 'sign-up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('index')
        else:
            error_msg = 'Invalid Credentials'
            messages.error(request, error_msg)
            return redirect('sign_in')
    return render(request, 'sign-in.html')

@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    msg = 'Successfully Signed Out'
    messages.success(request, msg)
    return redirect('sign_in')