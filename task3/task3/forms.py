from django import forms

class MyForm(forms.Form):
    first_number = forms.IntegerField(label='first number',required=True)
    second_number = forms.IntegerField(label='second number',required=True)
    first_number.widget.attrs['class'] = 'form-control'
    second_number.widget.attrs['class'] = 'form-control'
