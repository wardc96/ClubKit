from django import forms
from clubkit.rentapitch.models import RentPitch
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Form to obtain pitch rental information
class RentalForm(forms.ModelForm):
    class Meta():
        model = RentPitch
        fields = ('club_id', 'pitch_id', 'name', 'email',
                  'mobile', 'date', 'start_time', 'finish_time')
        widgets = {
            'date': forms.DateInput(attrs={'id': 'datepicker'}),
            'start_time': forms.DateInput(attrs={'class': 'timepicker'}),
            'finish_time': forms.DateInput(attrs={'class': 'timepicker'})
        }

        def clean_date(self):
            date = self.clean_date['date']
            if date < datetime.date.today():
                raise ValidationError(_('Date cannot be in the past.'))
            return date

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()



