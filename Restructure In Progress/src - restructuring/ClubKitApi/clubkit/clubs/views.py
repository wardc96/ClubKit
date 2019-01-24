from django.shortcuts import render, redirect
from clubkit.clubs.forms import ClubInfoForm
from clubkit.clubs.models import ClubInfo, Team, Pitch
from clubkit.clubs.serializers import TeamSerializer, PitchSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


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

