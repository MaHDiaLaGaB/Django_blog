from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# create django form
def register(request):
    if request.method == 'POST':
        # make post request to submit the form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # take the clean username
            username = form.cleaned_data.get('username')
            # show alert that form submit successfully
            messages.success(request, f'Your account has been created {username}!')
            return redirect('bolg-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
