from django import forms
from book.models import Transaction
from datetime import datetime
import json

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('user', 'date_time', 'description', 'detail',)
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

        # Test input a default JSON object to `detail` column:
        self.fields['detail'].initial = json.loads('{"name": "John", "age": 30, "city": "New York"}')
        # self.fields['detail'].widget = forms.HiddenInput()


class MyModelSearchForm(forms.Form):
    description_filter = forms.CharField(max_length=255, required=False)