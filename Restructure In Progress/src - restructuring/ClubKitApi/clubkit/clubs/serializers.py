from clubkit.clubs.models import Pitch, Team, ClubPosts
from rest_framework import serializers


class PitchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pitch
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class ClubPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClubPosts
        fields = '__all__'


