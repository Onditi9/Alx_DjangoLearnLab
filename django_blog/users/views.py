# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after successful registration
            return redirect('blog-home')  # redirects to home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

from .forms import UserRegisterForm, UserUpdateForm

# Profile view (requires login)
@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'u_form': u_form})
