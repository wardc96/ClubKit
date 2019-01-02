from django.contrib.auth.models import User, Group
from clubkit.api.models import PlayerRegistration
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
        model = PlayerRegistration
        fields = '__all__'
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }


'''
    def create(self, validated_data):
        return PlayerRegistration.objects.create(**validated_data)

'''