from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from clubkit.main.forms import UserForm, ClubInfoForm
from clubkit.clubs.models import ClubInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        users = User.objects.all()
        all_clubs = ClubInfo.objects.all()

        args = {'users': users,
                'all_clubs': all_clubs}
        return render(request, self.template_name, args)


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
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


class OurClubs(TemplateView):
    template_name = 'our_clubs.html'

    def get(self, request):
        all_clubs = ClubInfo.objects.all()
        args = {'all_clubs': all_clubs}
        return render(request, self.template_name, args)


