from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    projects = Projects.objects.all()
    context = {
        "projects":projects,
    }
    return render(request, 'home.html', context)