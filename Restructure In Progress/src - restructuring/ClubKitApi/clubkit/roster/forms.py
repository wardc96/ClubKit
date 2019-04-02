from django import forms
from clubkit.roster.models import RosterId
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RosterForm(forms.ModelForm):

    class Meta():
        model = RosterId
        fields = ('club_id', 'pitch_id', 'team_id', 'date',
                  'start_time', 'finish_time', 'reoccuring_event',)
        widgets = {
            'date': forms.DateInput(attrs={'id': 'datepicker'})
        }

        def clean_date(self):
            date = self.clean_date['date']
            if date < datetime.date.today():
                raise ValidationError(_('Date cannot be in the past.'))
            return date

    def __init__(self, *args, **kwargs):
        super(RosterForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()




