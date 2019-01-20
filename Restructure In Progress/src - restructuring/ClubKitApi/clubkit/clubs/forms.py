from django import forms
from clubkit.clubs.models import ClubInfo


class ClubInfoForm(forms.ModelForm):

    class Meta():
        model = ClubInfo
        fields = ('club_name', 'club_logo', 'club_address1', 'club_address2',
                  'club_address3', 'club_town', 'club_county', 'club_country',)

