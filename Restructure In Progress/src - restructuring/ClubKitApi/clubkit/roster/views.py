from clubkit.roster.models import RosterId, ClubInfo
from clubkit.roster.serializers import ClubRosterSerializer
from clubkit.roster.forms import RosterForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime, json


class ClubRoster(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'roster.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        form = RosterForm()
        # user = ClubInfo.objects.filter(user=request.user).first()
        roster = RosterId.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'roster': roster,
                         'club_pk': club_pk
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

'''
def event(request):
    all_events = RosterId.objects.all()
    get_event_types = RosterId.objects.only('club_id')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:
        event_arr = []
        if request.GET.get('club_id') == "all":
            all_events = RosterId.objects.all()
        else:
            all_events = RosterId.objects.filter(event_type__icontains=request.GET.get('club_id'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['team'] = i.team_id
            date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['date'] = date
            start_time = datetime.datetime.strptime(str(i.start_time.time()), '%H:%M:%S').strftime('%H:%M:%S')
            event_sub_arr['start_time'] = start_time
            end_time = datetime.datetime.strptime(str(i.finish_time.time()), '%H:%M:%S').strftime('%H:%M:%S')
            event_sub_arr['end_time'] = end_time
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        "get_event_types":get_event_types,

    }
    return render(request, 'roster.html', context)

'''