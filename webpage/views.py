from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def callback(request):
    return render(request,'callback.html')

def login(request):
    return render(request,'login.html')

def frontendDomination(request):
    return render(request,'frontendDomination.html')

def backendDomination(request):
    return render(request,'backendDomination.html')

def aptitude(request):
    return render(request,'aptitude.html')

def DSA(request):
    return render(request,'DSA.html')
