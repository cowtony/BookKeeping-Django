from django import forms
from book.models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('time',
                  "description",
                  "asset",
                  "expense",
                  "revenue",
                  "liability")