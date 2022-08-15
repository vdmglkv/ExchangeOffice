from django import forms
from .models import Operation


class Convert(forms.ModelForm):

    class Meta:
        model = Operation
        fields = ['From', 'value', 'To', 'result']
        widgets = {
            'result': forms.TextInput(attrs={'readonly': 'readonly'})
        }
