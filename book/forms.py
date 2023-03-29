from django import forms
from book.models import Transaction
from datetime import datetime

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('user', 'date_time', 'description',
                  'asset', 'expense', 'revenue', 'liability',)
        widgets = {
            'date_time': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S'),
            # 'date': forms.NumberInput(attrs={'type': 'date'}),  # Example of Date picker
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user.id
            self.fields['user'].widget = forms.HiddenInput()
        