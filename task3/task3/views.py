from task3.forms import MyForm
from django.http import HttpResponse
from django.shortcuts import render

def calculate(request):
    if(request.method == 'POST'):
        form = MyForm(request.POST)
        if form.is_valid():
           x = form.cleaned_data['first_number']
           y = form.cleaned_data['second_number']
           add = x + y
           sub = x - y   
           multiply = x * y   
           division = x / y   
           mod = x % y   
        result = '''
add = {addf}
sub = {subf}
multibly = {multiplyf}
division = {divisionf}
mod = {modf}
        '''.format( subf=sub , addf = add , multiplyf = multiply , divisionf = division , modf=mod)
        # return HttpResponse("Result = " + str(z))
        return render(request , 'index.html' ,{
            'result' : str(result),
            'form' : form
        })

    else:
        form =  MyForm()
        return render(request , 'index.html' , {'form' : form})