from clubkit.roster.models import RosterId
from rest_framework import serializers


class ClubRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = RosterId
        fields = '__all__'

