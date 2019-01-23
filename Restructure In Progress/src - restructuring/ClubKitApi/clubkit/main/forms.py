from django import forms
from clubkit.clubs.models import ClubInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = User.objects.create(first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],
                                   email=self.cleaned_data['email'],
                                   username=self.cleaned_data['username'],
                                   password=self.cleaned_data['password1']
                                   )

        if commit:
            user.save()

        return user


class ClubInfoForm(forms.ModelForm):

    class Meta():
        model = ClubInfo
        fields = ('club_name', 'club_logo', 'club_address1', 'club_address2',
                  'club_address3', 'club_town', 'club_county', 'club_country',)



