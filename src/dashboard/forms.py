from django import forms
from tracker.models import Expense,Income 

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['spent_amount', 'category', 'date', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select category'
        self.fields['date'].widget.attrs['type'] = 'date'
        
        
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['earned_amount', 'category', 'date', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select category'
        self.fields['date'].widget.attrs['type'] = 'date'