from django import forms

class MyForm(forms.Form):
    number = forms.IntegerField(label='number', required=True)
    number.widget.attrs['class'] = 'form-control'