from clubkit.player_register.serializers import PlayerRegistrationSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse


class RegisterPlayer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'player_registration.html'

    def get(self, request):
        serializer = PlayerRegistrationSerializer()
        return Response({'serializer': serializer,
                         })

    def post(self, request):
        serializer = PlayerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(template_name='player_registration_complete.html')
