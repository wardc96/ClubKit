from django.shortcuts import render, redirect
from clubkit.clubs.forms import ClubInfoForm, TeamForm, PitchForm, ClubPostForm, MembershipsForm
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts, ClubMemberships
from clubkit.clubs.serializers import TeamSerializer, PitchSerializer, ClubPostsSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from rest_framework import status
from rest_framework import serializers
from django.http import HttpResponse
from django.template import loader


def club_home(request, pk=None):
    if pk:
        request.session['pk'] = pk
        club = ClubInfo.objects.filter(pk=pk)
        club_posts = ClubPosts.objects.filter(club_id=club[0])
        args = {'club': club,
                'club_posts': club_posts,
                }
    else:
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_posts = ClubPosts.objects.filter(club_id=club[0])
        args = {'club': club,
                'club_posts': club_posts,
                'club_pk': club_pk
                }
    return render(request, 'club_home_page.html', args)


def edit_club(request):
    instance = ClubInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ClubInfoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')
        else:
            return redirect('clubs:club_home')
    else:
        form = ClubInfoForm(instance=instance)
        return render(request, 'edit_club.html', {'form': form})


class ClubAddPosts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_post.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info
        }
        form = ClubPostForm(initial=inital_data)
        club_post = ClubPosts.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'club_post': club_post,
                         'club_pk': club_pk
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


def delete_post(request, pk):
    club_post = ClubPosts.objects.filter(pk=pk)
    club_post.delete()
    return redirect('clubs:club_home')


def edit_post(request, pk):
    instance = ClubPosts.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ClubPostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')
        else:
            return redirect('clubs:club_home')
    else:
        form = ClubPostForm(instance=instance)
        return render(request, 'edit_post.html', {'form': form,
                                                  'instance': instance})


class TeamInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams.html'

    def get(self, request):
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            teams = Team.objects.filter(club_id=club_pk)
            club_info = ClubInfo.objects.filter(user=request.user).first()
            inital_data = {
                'club_id': club_info
            }
            form = TeamForm(initial=inital_data)
            return Response({
                'form': form,
                'teams': teams,
                'club_pk': club_pk
            })
        else:
            club_pk = request.session.get('pk')
            teams = Team.objects.filter(club_id=club_pk)
            return Response({
                             'teams': teams,
                             'club_pk': club_pk
                             })

    def post(self, request):
        form = TeamForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('clubs:teams')


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
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            club_info = ClubInfo.objects.filter(user=request.user).first()
            inital_data = {
                'club_id': club_info
            }
            form = PitchForm(initial=inital_data)
            pitch = Pitch.objects.filter(club_id=club_pk)
            return Response({'form': form,
                             'pitch': pitch,
                             'club_pk': club_pk
                             })
        else:
            club_pk = request.session.get('pk')
            pitch = Pitch.objects.filter(club_id=club_pk)
            return Response({'pitch': pitch,
                             'club_pk': club_pk
                             })

    def post(self, request):
        form = PitchForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('clubs:pitches')


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


class Memberships(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'memberships.html'

    def get(self, request):
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            club_info = ClubInfo.objects.filter(user=request.user).first()
            inital_data = {
                'club_id': club_info
            }
            form = MembershipsForm(initial=inital_data)
            # user = ClubInfo.objects.filter(user=request.user).first()
            memberships = ClubMemberships.objects.filter(club_id=club_pk)
            return Response({'form': form,
                             'memberships': memberships,
                             'club_pk': club_pk
                             })
        else:
            club_pk = request.session.get('pk')
            memberships = ClubMemberships.objects.filter(club_id=club_pk)
            return Response({'memberships': memberships,
                             'club_pk': club_pk
                             })

    def post(self, request):
        form = MembershipsForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('clubs:memberships')


def delete_membership(request, pk):
    memberships = ClubMemberships.objects.filter(pk=pk)
    memberships.delete()
    return redirect('clubs:memberships')


def edit_membership(request, pk):
    instance = ClubMemberships.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = MembershipsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:memberships')
        else:
            return redirect('clubs:memberships')
    else:
        form = MembershipsForm(instance=instance)
        return render(request, 'edit_membership.html', {'form': form,
                                                        'instance': instance})


