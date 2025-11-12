from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    return render(request, 'main/login.html')

def signup_view(request):
    return render(request, 'main/signup.html')
