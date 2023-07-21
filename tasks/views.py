from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # No necesitas User.save() aquí, ya que create_user ya guarda el usuario creado.
                return HttpResponse('User created successfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('Passwords do not match')