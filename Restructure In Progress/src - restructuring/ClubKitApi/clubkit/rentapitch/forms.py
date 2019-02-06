from django import forms
from clubkit.rentapitch.models import RentPitch
from clubkit.clubs.models import Pitch


class RentalForm(forms.ModelForm):

    class Meta():
        model = RentPitch
        fields = ('club_id', 'pitch_id', 'rental_cost', 'name', 'email',
                  'mobile', 'date', 'start_time', 'finish_time', 'payment_type', 'is_cancelled',)

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        # self.fields['club_id'] = forms.HiddenInput()



