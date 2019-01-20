from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from clubkit.profiles.forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


'''
def password_reset(request):
        email = UserForm.email
        return render(request, 'password_reset_form.html',
                      {'email': email})


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def password_reset_confirm(request):
        return render(request, 'password_reset_confirm.html')


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')
'''

