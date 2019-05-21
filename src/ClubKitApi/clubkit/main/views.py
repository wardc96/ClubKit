from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from clubkit.main.forms import UserForm, ClubInfoForm
from clubkit.clubs.forms import ClubPackagesForm
from clubkit.main.models import OurPackages
from clubkit.clubs.models import ClubInfo, ClubPackages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.db import transaction


# Class to handle index page information
class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        try:
            del request.session['cart']
        except KeyError:
            pass
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


# Method to display registration form and handle new registered users
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ClubInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            with transaction.atomic():
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
                package = ClubPackages()
                package.club_id = profile
                package.save()
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


# Method to handle user log in
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


# Class to display our clubs
class OurClubs(TemplateView):
    template_name = 'our-clubs.html'

    # Method to retrieve all clubs registered
    def get(self, request):
        all_clubs = ClubInfo.objects.all()
        args = {'all_clubs': all_clubs}
        return render(request, self.template_name, args)


# Class to display our packages
class Packages(TemplateView):
    template_name = 'our-packages.html'

    # Method to retrieve all packages
    def get(self, request):
        packages = OurPackages.objects.all()
        args = {'packages': packages}
        return render(request, self.template_name, args)


# Method to get all available packages to purchase
def purchase_packages(request):
    if request.user.is_authenticated:
        user = ClubInfo.objects.filter(user=request.user).first()
        packages = ClubPackages.objects.filter(club_id=user.pk).first()
        if request.method == 'POST':
            form = ClubPackagesForm(request.POST, instance=packages)
            if form.is_valid():
                form.club_id = ClubInfo.objects.get(user=request.user)
                form.save()
                return redirect('main:buy_packages')
            else:
                return redirect('main:buy_packages')
        else:
            form = ClubPackagesForm(instance=packages)
            return render(request, 'buy_now.html', {'form': form,
                                                    'user': user,
                                                    'packages': packages,
                                                    })
    else:
        return render(request, 'unautorized_user_landing_page.html')


# Method to render our about us page
def about_us(request):
    return render(request, 'about-us.html')


# Method to render our contact us page
def contact_us(request):
    return render(request, 'contact-us.html')




