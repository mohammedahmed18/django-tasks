from datetime import datetime
from django import forms

class MyForm(forms.Form):
    levels = (
        (1 , 'beginner'),
        (2 , 'intermediate'),
        (3 , 'Advanced'),
    )
    departments_choices = (
        ('cs' , 'computer science'),
        ('IT' , 'Information technology'),
        ('Ai' , 'Artificial initiligance'),
        ('MI' , 'Medical informatics'),
    )
    num = forms.IntegerField(label="your age" , required=True)
    name = forms.CharField(label="your name" , required=True)
    is_student = forms.BooleanField(label="Are you a student" , required=False)
    level = forms.ChoiceField(label="your level" ,choices=levels ,required=True)
    birthday = forms.DateField(label="your birthday" , initial=datetime.now())
    start_day = forms.DateTimeField(label="start day" , initial=datetime.now())
    departments = forms.MultipleChoiceField(label="departments" ,choices=departments_choices)


    num.widget.attrs['class'] = 'form-control mb-3 mt-1'
    name.widget.attrs['class'] = 'form-control mb-3 mt-1'
    level.widget.attrs['class'] = 'form-control mb-3 mt-1'
    birthday.widget.attrs['class'] = 'form-control mb-3 mt-1'
    start_day.widget.attrs['class'] = 'form-control mb-3 mt-1'
    departments.widget.attrs['class'] = 'form-control mb-3 mt-1'
    is_student.widget.attrs['class'] = 'checkbox'