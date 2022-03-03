from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



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


# change the profile info from the form
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been updated')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
