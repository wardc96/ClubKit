from clubkit.player_register.forms import PlayerRegistrationForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from clubkit.clubs.models import ClubInfo, ClubMemberships


# Class to handle membership registration information
class RegisterPlayer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'player_registration.html'

    # Get method membership information and registration from
    def get(self, request):
        club_pk = request.session.get('pk')
        club_info = ClubInfo.objects.filter(pk=club_pk).first()
        club_memberships = ClubMemberships.objects.filter(club_id=club_info)
        inital_data = {
            'club_id': club_info,
            'membership_title': club_memberships,
            'club_pk': club_pk
        }
        form = PlayerRegistrationForm(initial=inital_data)
        form.fields['membership_title'].queryset = ClubMemberships.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'club_pk': club_pk
                         })

    # Post method to save player registration
    def post(self, request):
        form = PlayerRegistrationForm(data=request.data)
        if form.is_valid():
            form.save()
            return Response(template_name='player_registration_complete.html')
