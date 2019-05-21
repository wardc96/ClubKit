from django import forms
from django.contrib.auth.models import User


# Form to allow users to edit profile information
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name')




