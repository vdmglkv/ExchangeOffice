from django import forms


class Convert(forms.Form):
    currency_from = forms.ChoiceField(choices=(('1', 'USD'), ('2', 'EUR'), ('3', 'BYN')), label='From')
    value_from = forms.DecimalField(required=False, initial=0, label='Amount')
    currency_to = forms.ChoiceField(choices=(('1', 'USD'), ('2', 'EUR'),  ('3', 'BYN')), label='To')
    value_to = forms.DecimalField(required=False, initial=0, label='Amount')
