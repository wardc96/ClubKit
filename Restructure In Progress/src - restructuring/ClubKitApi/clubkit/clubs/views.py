from django.shortcuts import render, redirect
from clubkit.clubs.forms import ClubInfoForm, TeamForm, PitchForm
from clubkit.clubs.models import ClubInfo, Team, Pitch
from clubkit.clubs.serializers import TeamSerializer, PitchSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.http import HttpResponse
from django.template import loader


def club_home(request, pk=None):
    if pk:
        club = ClubInfo.objects.filter(pk=pk)
    elif request.user.is_authenticated:
        club = ClubInfo.objects.filter(user=request.user)
    # photo = model.club_logo.ImageField(storage=profile_pics)
    args = {'club': club,
            }
    return render(request, 'club_home_page.html', args)


def edit_club(request):
    instance = ClubInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ClubInfoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = ClubInfoForm(instance=instance)
        return render(request, 'edit_club.html', {'form': form})


class TeamInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams.html'

    def get(self, request):

        serializer = TeamSerializer()
        user = ClubInfo.objects.filter(user=request.user).first()
        teams = Team.objects.filter(club_id=user.pk)
        return Response({'serializer': serializer,
                         'teams': teams
                         })

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        teams = Team.objects.filter(club_id=user.pk)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer,
                             'teams': teams
                             })


def delete_team(request, pk):
    team = Team.objects.filter(pk=pk)
    team.delete()
    return redirect('clubs:teams')


def edit_team(request, pk):
    instance = Team.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:teams')
        else:
            return redirect('clubs:teams')
    else:
        form = TeamForm(instance=instance)
        return render(request, 'edit_team.html', {'form': form,
                                                  'instance': instance})


'''
def edit_team(request, pk):
    instance = Team.objects.filter(pk=pk)
    if request.method == 'POST':
        serializer = TeamSerializer(request.POST, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        serializer = TeamSerializer(instance=instance)
        return render(
            request,
            'edit_team.html',
            {'serializer': serializer, 'instance': instance})

'''


class PitchInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitches.html'

    def get(self, request):

        serializer = PitchSerializer()
        user = ClubInfo.objects.filter(user=request.user).first()
        pitch = Pitch.objects.filter(club_id=user.pk)
        return Response({'serializer': serializer,
                         'pitch': pitch
                         })

    def post(self, request):
        serializer = PitchSerializer(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        pitch = Pitch.objects.filter(club_id=user.pk)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer,
                             'pitch': pitch
                             })


def delete_pitch(request, pk):
    pitch = Pitch.objects.filter(pk=pk)
    pitch.delete()
    return redirect('clubs:pitches')


def edit_pitch(request, pk):
    instance = Pitch.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = PitchForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:pitches')
        else:
            return redirect('clubs:pitches')
    else:
        form = PitchForm(instance=instance)
        return render(request, 'edit_pitch.html', {'form': form,
                                                   'instance': instance})

'''
def edit_pitch(request, pk):
    instance = Pitch.objects.filter(pk=pk)
    if request.method == 'POST':
        serializer = PitchSerializer(request.POST, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        serializer = PitchSerializer(instance=instance)
        return render(request, 'edit_pitch.html', {'serializer': serializer})

'''
