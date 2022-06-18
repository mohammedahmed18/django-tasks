from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=200,min_length=3,label="name", required=True)
    email = forms.EmailField(label='email', required=True)
    phone = forms.CharField(max_length=11,label='phone_number',required=True)    
    name.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    phone.widget.attrs['class'] = 'form-control'