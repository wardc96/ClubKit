from django import forms
from clubkit.roster.models import RosterId


class RosterForm(forms.ModelForm):

    class Meta():
        model = RosterId
        fields = ('club_id', 'pitch_id', 'team_id', 'date',
                  'start_time', 'finish_time')

    def __init__(self, *args, **kwargs):
        super(RosterForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()

