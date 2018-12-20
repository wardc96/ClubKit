from django.contrib.auth.models import User
from rest_framework import viewsets
from clubkit.api.serializers import UserSerializer
from django.shortcuts import render, redirect
from clubkit.api.forms import UserForm, ClubInfoForm
from clubkit.api.models import ClubInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage

profile_pics = FileSystemStorage(location='clubkit/media/profile_pics')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    '''
    Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
    We can easily break these down into individual views if we need to, 
    but using viewsets keeps the view logic nicely organized as well as being very concise.
    '''


def index(request):
    return render(request, 'index.html')


@login_required
def special():
    return redirect('/account/club_home')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ClubInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ClubInfoForm()
    return render(request,
                  'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'club_home_page.html', {})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


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


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def club_home(request):
    model = ClubInfo.objects.filter(user=request.user)
    # photo = model.club_logo.ImageField(storage=profile_pics)
    args = {'model': model,
            }
    return render(request, 'club_home_page.html', args)


def edit_club(request):
    if request.method == 'POST':
        form = ClubInfoForm(data=request.POST, instance=request.kwargs)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.kwargs)
            return redirect('/account/club_home')
    else:
        form = ClubInfoForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_club.html', args)







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

