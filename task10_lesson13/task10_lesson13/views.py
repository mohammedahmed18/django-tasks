from task10_lesson13.forms import MyForm
from django.shortcuts import render

# Create your views here.
def first(req):
    if req.method == 'POST':
        form = MyForm(req.POST)
        if form.is_valid():
            msg = form.cleaned_data['msg']
            return render(req , 'task10/index.html',{"form" : form , 'msg' : msg})
        
    else:
        form = MyForm()
        return render(req , 'task10/index.html',{"form" : form})
