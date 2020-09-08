from django import forms
from .models import DetailCard


class DetailForm(forms.ModelForm):
    class Meta():
        model = DetailCard
        fields = ['credit_card_number', 'card_holder',
                  'expiration_date', 'security_code', 'amount']
        widgets = {
            'credit_card_number': forms.TextInput(attrs={'placeholder': '4444-4444-4444-4444'}),
            'card_holder': forms.TextInput(attrs={'placeholder': 'Name on the Card'}),
            'expiration_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'security_code': forms.TextInput(attrs={'placeholder': '3 numbers'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Specify the amount'}),
        }
