from django import forms
from clubkit.player_register.models import Player
from django.forms.widgets import DateInput


# Form to accept details for members to register
class PlayerRegistrationForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'dob': 'Date of Birth'
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(PlayerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()



