from django import forms

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label='Первое число', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    num2 = forms.FloatField(label='Второе число', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    operation = forms.ChoiceField(
        label='Действие',
        choices=[
            ('+', '+'),
            ('-', '-'),
            ('*', '*'),
            ('/', '/'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )