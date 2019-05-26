from django import forms
from clubkit.player_register.models import Player
from clubkit.clubs.models import ClubMemberships
from django.forms.widgets import DateInput


# Form to accept details for members to register
class PlayerRegistrationForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'dob': 'Date of Birth (yyyy-mm-dd)'
        }
        widgets = {
            'dob': forms.DateInput(attrs={'id': 'datepicker'})
        }

        '''
        def load_price(self):
            mem_title = self.get['membership_title']
            if ClubMemberships.objects.filter(title=mem_title).exists():
                return mem_title
            self.fields['price'] = ClubMemberships.objects.filter(title=mem_title).values('price')
        '''

    def __init__(self, *args, **kwargs):
        super(PlayerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()
        # self.fields['price'].widget = forms.HiddenInput()
        # self.fields['price'].queryset = ClubMemberships.objects.none()







