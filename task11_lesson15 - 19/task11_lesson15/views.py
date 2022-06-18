import json
from django.http import  JsonResponse
from django.shortcuts import render
from task11_lesson15.forms import MyForm
from dateutil.parser import parse




def is_valid_date(date):
    if date:
        try:
            parse(date)
            return True
        except:
            return False
    return False




def get_level_name(level_num):
    if level_num == '1':
        return 'beginner'
    elif level_num == '2':
        return 'intermediate'
    else:
        return 'Advanced'

def index(req):
    if req.method == 'POST':
        form = MyForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['is_student'] = 'student' if data['is_student'] else 'not a student'
            data['level'] = get_level_name(data['level'])
            return render(req , 'index.html' , {'form' : form , "data" : data})
        else:
            return render(req , 'index.html' , {'form' : form , 'errors' : form.errors})
    else:
        form = MyForm()
        return render(req , 'index.html' , {'form' : form})