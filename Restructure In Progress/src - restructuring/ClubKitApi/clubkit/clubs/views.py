from django.shortcuts import render, redirect
from clubkit.clubs.forms import ClubInfoForm, TeamForm, PitchForm, ClubPostForm
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts
from clubkit.clubs.serializers import TeamSerializer, PitchSerializer, ClubPostsSerializer
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
        club_posts = ClubPosts.objects.filter(club_id=club[0])
    elif request.user.is_authenticated:
        club = ClubInfo.objects.filter(user=request.user)
        club_posts = ClubPosts.objects.filter(club_id=club[0])
    # photo = model.club_logo.ImageField(storage=profile_pics)
    args = {'club': club,
            'club_posts': club_posts
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


class ClubAddPosts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_post.html'

    def get(self, request):

        form = ClubPostForm()
        user = ClubInfo.objects.filter(user=request.user).first()
        club_post = ClubPosts.objects.filter(club_id=user.pk)
        return Response({'form': form,
                         'club_post': club_post
                         })

    def post(self, request):
        form = ClubPostForm(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        new_post = ClubPosts.objects.filter(club_id=user.pk)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')
        else:
            return Response({'form': form,
                             'new_post': new_post
                             })


'''
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

