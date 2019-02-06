from django import forms
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts, ClubMemberships


class ClubInfoForm(forms.ModelForm):

    class Meta():
        model = ClubInfo
        fields = ('club_name', 'club_logo', 'club_address1', 'club_address2',
                  'club_address3', 'club_town', 'club_county', 'club_country',)


class TeamForm(forms.ModelForm):

    class Meta():
        model = Team
        fields = ('club_id', 'team_name', 'manager_name')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        # self.fields['club_id'].widget = forms.HiddenInput()


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
