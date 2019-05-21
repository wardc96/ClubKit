from django import forms
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts, ClubMemberships, ClubPackages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Form to update/change club information
class ClubInfoForm(forms.ModelForm):
    club_address2 = forms.CharField(required=False)
    club_address3 = forms.CharField(required=False)

    class Meta():
        model = ClubInfo
        fields = ('club_name', 'club_logo', 'club_address1', 'club_address2',
                  'club_address3', 'club_town', 'club_county', 'club_country',)

        def clean_club_name(self):
            club_name = self.cleaned_data['club_name']
            if ClubInfo.objects.filter(club_name=club_name).exists():
                raise ValidationError(_("Club already exists"))
            return club_name


# Form to obtain club team information
class TeamForm(forms.ModelForm):

    class Meta():
        model = Team
        fields = ('club_id', 'team_name', 'manager_name')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()

    def clean_team_name(self):
        team_name = self.cleaned_data['team_name']
        if Team.objects.filter(team_name=team_name).exists():
            raise ValidationError(_("Team already exists"))
        return team_name


# Form to obtain club pitch information
class PitchForm(forms.ModelForm):

    class Meta():
        model = Pitch
        fields = ('club_id', 'pitch_name', 'pitch_size', 'pitch_type', 'open_time',
                  'close_time', 'rental', 'rental_price', 'max_people')

    def __init__(self, *args, **kwargs):
        super(PitchForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()


# Form to obtain club post information
class ClubPostForm(forms.ModelForm):

    class Meta():
        model = ClubPosts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClubPostForm, self).__init__(*args, **kwargs)
        self.fields['created_date'].widget = forms.HiddenInput()
        self.fields['club_id'].widget = forms.HiddenInput()


# Form to obtain club membership information
class MembershipsForm(forms.ModelForm):

    class Meta():
        model = ClubMemberships
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MembershipsForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()


# Form to handle club access to packages
class ClubPackagesForm(forms.ModelForm):

    class Meta():
        model = ClubPackages
        fields = ('club_id', 'player_register_package', 'roster_package', 'rent_a_pitch_package', 'shop_package')

    def __init__(self, *args, **kwargs):
        super(ClubPackagesForm, self).__init__(*args, **kwargs)










