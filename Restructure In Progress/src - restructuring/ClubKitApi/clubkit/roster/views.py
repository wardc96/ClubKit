from clubkit.roster.models import RosterId, ClubInfo
from clubkit.roster.serializers import ClubRosterSerializer
from clubkit.roster.forms import RosterForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


class ClubRoster(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'roster.html'

    def get(self, request):

        form = RosterForm()
        user = ClubInfo.objects.filter(user=request.user).first()
        roster = RosterId.objects.filter(club_id=user.pk)
        return Response({'form': form,
                         'roster': roster
                         })

    def post(self, request):
        form = RosterForm(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        roster = RosterId.objects.filter(club_id=user.pk)
        if form.is_valid():
            form.save()
            return Response({'form': form,
                             'roster': roster
                             })


def delete_roster(request, pk):
    roster = RosterId.objects.filter(pk=pk)
    roster.delete()
    return redirect('roster:club_roster')


def edit_roster(request, pk):
    instance = RosterId.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = RosterForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('roster:club_roster')
        else:
            return redirect('roster:club_roster')
    else:
        form = RosterForm(instance=instance)
        return render(request, 'edit_roster.html', {'form': form,

                                                    'instance': instance})
'''
def edit_roster(request, pk):
    instance = RosterId.objects.filter(pk=pk)
    if request.method == 'POST':
        serializer = ClubRosterSerializer(request.POST, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        serializer = ClubRosterSerializer(instance=instance)
        return render(request, 'edit_roster.html', {'serializer': serializer})

'''
