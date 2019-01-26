from clubkit.roster.models import RosterId, ClubInfo
from clubkit.roster.serializers import ClubRosterSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect


class ClubRoster(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'roster.html'

    def get(self, request):

        serializer = ClubRosterSerializer()
        user = ClubInfo.objects.filter(user=request.user).first()
        roster = RosterId.objects.filter(club_id=user.pk)
        return Response({'serializer': serializer,
                         'roster': roster
                         })

    def post(self, request):
        serializer = ClubRosterSerializer(data=request.data)
        user = ClubInfo.objects.filter(user=request.user).first()
        roster = RosterId.objects.filter(club_id=user.pk)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer,
                             'roster': roster
                             })


def delete_roster(request, pk):
    roster = RosterId.objects.filter(pk=pk)
    roster.delete()
    return redirect('roster:club_roster')


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


