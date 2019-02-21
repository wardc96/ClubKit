from django import forms
from clubkit.clubs.models import ClubInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Email already exists"))
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(_("Username already exists"))
        return username

    def clean_password(self):
        form_data = self.cleaned_data
        if form_data['password1'] != form_data['password2']:
            self._errors["password1"] = ["Password do not match"]  # Will raise a error message
            del form_data['password1']
        return form_data

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
    club_address2 = forms.CharField(required=False)
    club_address3 = forms.CharField(required=False)

    class Meta():
        model = ClubInfo
        fields = ('club_name', 'club_logo', 'club_address1', 'club_address2',
                  'club_address3', 'club_town', 'club_county', 'club_country',)

        def clean_club_name(self):
            club_name = self.cleaned_data['club_name']
            if ClubInfo.objects.filter(club_name=club_name).exists():
                raise ValidationError(_("Club already exists"))
            return club_name



