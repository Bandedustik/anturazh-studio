from django import forms
from landingPage.models import Client

class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
