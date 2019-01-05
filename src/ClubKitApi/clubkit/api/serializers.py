from django.contrib.auth.models import User, Group
from clubkit.api.models import Player, RosterId, Team, Pitch
from rest_framework import serializers
from django.forms.widgets import DateInput

'''
Notice that we're using hyperlinked relations in this case, with HyperlinkedModelSerializer.
You can also use primary key and various other relationships, but hyperlinking is good RESTful design.
'''


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class PlayerRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

        def validate_data(self, validate_data):
            first_name = validate_data['first_name']
            last_name = validate_data['last_name']
            name = Player(
                first_name=first_name,
                last_name=last_name
            )
            if not name:
                raise serializers.ValidationError("You need to include a name")


class ClubRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = RosterId
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class PitchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pitch
        fields = '__all__'

'''
    def create(self, validated_data):
        return PlayerRegistration.objects.create(**validated_data)

'''