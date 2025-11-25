from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from assignments.models import About
from blogs.models import Blog
from .forms import RegistrationForm

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="published")
    posts = Blog.objects.filter(is_featured=False, status="published")
    
    # Fetch about us information
    try:
        about = About.objects.get()
    except:
        about = None
        
    context = {
        "featured_posts": featured_posts,
        "posts": posts,
        "about": about,
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
            # You might want to log the user in or redirect them after registration
    else:
        form = RegistrationForm()
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect("home")
    
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect("home")