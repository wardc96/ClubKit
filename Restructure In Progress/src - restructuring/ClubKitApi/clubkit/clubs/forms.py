from django import forms
from django.contrib.auth.models import User
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts, ClubMemberships
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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


class TeamForm(forms.ModelForm):

    class Meta():
        model = Team
        fields = ('club_id', 'team_name', 'manager_name')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        # user = kwargs.pop('user', None)
        # self.fields['club_id'].queryset = ClubInfo.objects.filter(user=user.pk)

    def clean_team_name(self):
        team_name = self.cleaned_data['team_name']
        if Team.objects.filter(team_name=team_name).exists():
            raise ValidationError(_("Team already exists"))
        return team_name


class PitchForm(forms.ModelForm):

    class Meta():
        model = Pitch
        fields = ('club_id', 'pitch_name', 'pitch_size', 'pitch_type', 'open_time',
                  'close_time', 'rental', 'rental_price', 'max_people')

    def __init__(self, *args, **kwargs):
        super(PitchForm, self).__init__(*args, **kwargs)
        # self.fields['club_id'].widget = forms.HiddenInput()


class ClubPostForm(forms.ModelForm):

    class Meta():
        model = ClubPosts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClubPostForm, self).__init__(*args, **kwargs)
        self.fields['created_date'].widget = forms.HiddenInput()


class MembershipsForm(forms.ModelForm):

    class Meta():
        model = ClubMemberships
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MembershipsForm, self).__init__(*args, **kwargs)
