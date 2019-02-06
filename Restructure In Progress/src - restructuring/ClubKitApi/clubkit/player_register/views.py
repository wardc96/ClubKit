from clubkit.player_register.serializers import PlayerRegistrationSerializer
from clubkit.player_register.forms import PlayerRegistrationForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse


class RegisterPlayer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'player_registration.html'

    def get(self, request):
        form = PlayerRegistrationForm()
        return Response({'form': form,
                         })

    def post(self, request):
        form = PlayerRegistrationForm(data=request.data)
        if form.is_valid():
            form.save()
            return Response(template_name='player_registration_complete.html')
