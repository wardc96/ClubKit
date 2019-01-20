from clubkit.player_register.models import Player
from rest_framework import serializers
from django.forms.widgets import DateInput


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

