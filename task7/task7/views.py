from task7.forms import MyForm
from django.shortcuts import render

def index(req):
    numberOfForms = 4
    forms = []
    
    if req.method == 'POST':
        result = ''
        sum = 0
        for i in range(numberOfForms):
            form = MyForm(req.POST,prefix='form'+str(i+1))
            if form.is_valid():
                cd = form.cleaned_data
                num = int(cd['number']);
                sum += num
                if i == 0:
                    result += str(num)
                else:
                    result += "+"+str(num)
            forms.append(form)  

        return render(req , 'index.html',{"forms" : forms , 'result' : result , 'sum' : sum})
    else:
        forms = []
        for i in range(numberOfForms):
            form = MyForm(prefix='form'+str(i+1))
            forms.append(form)
    return render(req , 'index.html',{"forms" : forms})