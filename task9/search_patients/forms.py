from django.forms import CharField, forms


class MyForm(forms.Form):
    name = CharField(label='name' , required=True)
    name.widget.attrs['class'] = 'form-control'