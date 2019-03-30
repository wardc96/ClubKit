from django import forms
from clubkit.player_register.models import Player
from django.forms.widgets import DateInput


class PlayerRegistrationForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(PlayerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()



