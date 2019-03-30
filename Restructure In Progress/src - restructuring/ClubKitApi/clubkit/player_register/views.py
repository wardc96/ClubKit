from clubkit.player_register.serializers import PlayerRegistrationSerializer
from clubkit.player_register.forms import PlayerRegistrationForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from clubkit.clubs.models import ClubInfo, ClubMemberships
from django.urls import reverse


class RegisterPlayer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'player_registration.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club_info = ClubInfo.objects.filter(pk=club_pk).first()
        club_memberships = ClubMemberships.objects.filter(club_id=club_info)
        inital_data = {
            'club_id': club_info,
            'membership_title': club_memberships
        }
        form = PlayerRegistrationForm(initial=inital_data)
        return Response({'form': form,
                         })

    def post(self, request):
        form = PlayerRegistrationForm(data=request.data)
        if form.is_valid():
            form.save()
            return Response(template_name='player_registration_complete.html')
