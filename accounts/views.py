from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            newwriter = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            auth.login(request, newwriter)
            return redirect('main:firstpage')
    
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        writer = auth.authenticate(request, username=username, password=password)

        if writer is not None:
            auth.login(request, writer)
            return redirect('main:firstpage')
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('main:firstpage')