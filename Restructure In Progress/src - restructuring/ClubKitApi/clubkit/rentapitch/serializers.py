from clubkit.rentapitch.models import RentPitch
from rest_framework import serializers


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentPitch
        fields = '__all__'