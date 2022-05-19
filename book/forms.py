from django import forms
from book.models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('date', 'time', 'description',
                  'asset', 'expense', 'revenue', 'liability',)
        widgets = {
            'date': forms.NumberInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(),
        }