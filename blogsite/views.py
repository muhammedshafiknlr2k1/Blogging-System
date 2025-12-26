
from django.shortcuts import render, redirect
from blogs.models import Blogs
from core.models import About
from django.contrib import messages
from django.contrib.auth.models import Group 
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_posts = Blogs.objects.filter(
        is_featured=True, status='Published').order_by('-updated_at')
    posts = Blogs.objects.filter(is_featured=False, status='Published')
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('register')
#         else:
#             print(form.errors)
#     else:
#         form = RegistrationForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user instance
            user = form.save(commit=False)  # Do not commit yet
            user.is_active = True  # optional
            user.save()  # Save to DB

            # Assign user to default group 'User'
            # This works even if the group does not exist
            user_group, created = Group.objects.get_or_create(name='User')
            user.groups.add(user_group)  # Assign group

            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')

    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')