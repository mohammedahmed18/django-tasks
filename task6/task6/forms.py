from django import forms

class MyForm(forms.Form):
    num = forms.IntegerField(required = True , label='number')
