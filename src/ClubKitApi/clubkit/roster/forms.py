from django import forms
from clubkit.roster.models import RosterId, Pitch
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Form to add/edit club roster
class RosterForm(forms.ModelForm):

    class Meta():
        model = RosterId
        fields = ('club_id', 'pitch_id', 'team_id', 'date',
                  'start_time', 'finish_time', 'reoccuring_event', 'reoccuring_day')
        widgets = {
            'date': forms.DateInput(attrs={'id': 'datepicker'}),
            'start_time': forms.DateInput(attrs={'class': 'timepicker'}),
            'finish_time': forms.DateInput(attrs={'class': 'timepicker'})
        }
        labels = {
            'reoccuring_event': 'Repeat every week?',
            'reoccuring_day': 'Which day?'
        }

        def clean_date(self):
            date = self.clean_date['date']
            if date < datetime.date.today():
                raise ValidationError(_('Date cannot be in the past.'))
            return date

        '''
        def clean(self):
            date = self.cleaned_data.get('date')
            start_time = self.cleaned_data.get('start_time')
            finish_time = self.cleaned_data.get('finish_time')
            between = RosterId.objects.filter(date=date, start_time=start_time, finish_time=finish_time).exists()
            if between:
                raise forms.ValidationError("Period already between this dates")
            super(RosterForm, self).clean()
        '''

    def __init__(self, *args, **kwargs):
        super(RosterForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()











