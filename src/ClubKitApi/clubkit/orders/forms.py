from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['club_id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['club_id'].widget = forms.HiddenInput()
