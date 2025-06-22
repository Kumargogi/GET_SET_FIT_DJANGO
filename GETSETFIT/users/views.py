
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import SignupForm, LoginForm

def landing_page(request):
    return render(request, 'users/landing.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            # Check if this user exists in the database
            try:
                user = CustomUser.objects.get(name=name, password=password)
                return redirect('landing')  # Logged in!
            except CustomUser.DoesNotExist:
                form.add_error(None, "Invalid credentials")

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
