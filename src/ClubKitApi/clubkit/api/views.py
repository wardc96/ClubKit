from django.contrib.auth.models import User
from rest_framework import viewsets
from clubkit.api.serializers import UserSerializer, PlayerRegistrationSerializer
from django.shortcuts import render, redirect
from clubkit.api.forms import UserForm, ClubInfoForm, EditProfileForm, PlayerRegistrationForm
from clubkit.api.models import ClubInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        users = User.objects.all()
        clubs = ClubInfo.objects.all()

        args = {'users': users,
                'clubs': clubs}
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


class RegisterPlayer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'player_registration.html'

    def get(self, request):
        serializer = PlayerRegistrationSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = PlayerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html', {})
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


def club_home(request, pk=None):
    if pk:
        club = ClubInfo.objects.filter(pk=pk)
        user = request.user
    else:
        club = ClubInfo.objects.filter(user=request.user)
        user = request.user
    # photo = model.club_logo.ImageField(storage=profile_pics)
    args = {'club': club,
            'user': user
            }
    return render(request, 'club_home_page.html', args)


def edit_club(request):
        form = ClubInfoForm(request.POST or None, instance=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user.username = request.user
            instance.save()
            return redirect('/account/club_home')
        context = {
            'form': form,
        }
        return render(request, 'edit_club.html', context)



'''
class EditClub(TemplateView):
    template_name = 'edit_club.html'

    def get(self, request):
        form = ClubInfoForm()
        return render(request, self.template_name, {'form': form})

    def put(self, request):
        form = ClubInfoForm(request.PUT)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form = ClubInfoForm()
        context = {'form': form}
        return render(request, self.template_name, context)

'''

'''
if request.method == 'POST':
        form = ClubInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/club_home')

    else:
        form = ClubInfoForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_club.html', args)'''

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

