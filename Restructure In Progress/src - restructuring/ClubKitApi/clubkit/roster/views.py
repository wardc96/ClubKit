from clubkit.roster.models import RosterId
from clubkit.roster.serializers import ClubRosterSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class ClubRoster(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'edit_club_roster.html'

    def get(self, request):
        serializer = ClubRosterSerializer()
        roster = RosterId.objects.all()
        return Response({'serializer': serializer,
                         'roster': roster})

    def post(self, request):
        serializer = ClubRosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(template_name='roster_saved.html')


