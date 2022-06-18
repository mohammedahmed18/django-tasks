from django import forms

class MyForm(forms.Form):
    countries = forms.CharField(required = True , label='countries seperated by ,',widget=forms.Textarea)
    countries.widget.attrs['class'] = 'form-control'
