from django import forms
from clubkit.rentapitch.models import RentPitch
from clubkit.clubs.models import Pitch
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class RentalForm(forms.ModelForm):

    class Meta():
        model = RentPitch
        fields = ('club_id', 'pitch_id', 'rental_cost', 'name', 'email',
                  'mobile', 'date', 'start_time', 'finish_time', 'payment_type', 'is_cancelled',)


        def clean_date(self):
            date = self.clean_date['date']
            if date < datetime.date.today():
                raise ValidationError(_('Date cannot be in the past.'))
            return date

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()



