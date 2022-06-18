from django import forms

class MyForm(forms.Form):
    num = forms.IntegerField(label='number',required=True)
    num.widget.attrs['class'] = 'form-control'
