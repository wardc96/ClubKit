from django import forms
from clubkit.api.models import ClubInfo, Player
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import DateInput


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ClubInfoForm(forms.ModelForm):

    class Meta():
        model = ClubInfo
        fields = ('club_name', 'club_logo', 'club_address1', 'club_address2',
                  'club_address3', 'club_town', 'club_county', 'club_country',)


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name')


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



