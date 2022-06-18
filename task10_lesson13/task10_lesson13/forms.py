from django.forms import CharField, forms


class MyForm(forms.Form):
    msg = CharField(label="enter your message" , required=True)
    msg.widget.attrs['class'] = 'form-control'