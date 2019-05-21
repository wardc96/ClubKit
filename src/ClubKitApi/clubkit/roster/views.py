from clubkit.roster.models import RosterId, ClubInfo, Pitch
from clubkit.clubs.models import Team
from clubkit.roster.forms import RosterForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect


# Class to handle roster information
class ClubRoster(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'roster.html'

    # Get method to retrieve current roster information and form
    def get(self, request):
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            club_info = ClubInfo.objects.filter(user=request.user).first()
            reoccuring_event = RosterId.objects.filter(reoccuring_event=True, club_id=club_pk)
            inital_data = {
                'club_id': club_info,
            }
            form = RosterForm(initial=inital_data)
            form.fields['pitch_id'].queryset = Pitch.objects.filter(club_id=club_pk)
            form.fields['team_id'].queryset = Team.objects.filter(club_id=club_pk)
            roster = RosterId.objects.filter(club_id=club_pk)
            return Response({'form': form,
                             'roster': roster,
                             'club_pk': club_pk,
                             'reoccuring_event': reoccuring_event,
                             'club': club
                             })
        else:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            roster = RosterId.objects.filter(club_id=club_pk)
            reoccuring_event = RosterId.objects.filter(reoccuring_event=True, club_id=club_pk)
            return Response({'roster': roster,
                             'club_pk': club_pk,
                             'reoccuring_event': reoccuring_event,
                             'club': club
                             })

    # Post method to add roster information
    def post(self, request):
        form = RosterForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('roster:club_roster')


# Method to delete roster information
def delete_roster(request, pk):
    roster = RosterId.objects.filter(pk=pk)
    roster.delete()
    return redirect('roster:club_roster')


# Method to edit roster information
def edit_roster(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
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
                                                    'club': club,
                                                    'instance': instance})
