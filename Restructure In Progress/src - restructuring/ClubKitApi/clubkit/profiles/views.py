from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from clubkit.profiles.forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm


# Method used to change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profiles:view_profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


# Method used to view profile
def view_profile(request):
        user = request.user
        args = {'user': user}
        return render(request, 'profile.html', args)


# Method used to edit profile
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profiles:view_profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


