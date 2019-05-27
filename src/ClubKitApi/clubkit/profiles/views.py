from django.contrib.auth.models import User
from clubkit.clubs.models import ClubInfo
from django.shortcuts import render, redirect
from clubkit.profiles.forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm


# Method used to change password
def change_password(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profiles:view_profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form,
                'club': club}
        return render(request, 'change_password.html', args)


# Method used to view profile
def view_profile(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    user = request.user
    args = {'user': user,
            'club': club}
    return render(request, 'profile.html', args)


# Method used to edit profile
def edit_profile(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form,
                'club': club}
        return render(request, 'edit_profile.html', args)


