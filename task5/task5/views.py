import random 
from task5.forms import MyForm
from django.http import HttpResponse
from django.shortcuts import render



def wordlcup(request):
    m =''
    form = MyForm()
    if request.method =='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            x = cd['countries']
            y = x.split(',')
            for i in range(int(len(y)/2)):
                z = random.sample(y, k=2)
                for i in z:
                    y.remove(i)
                m +=   z[0]+ 'X' + z[1] +'\n'
            return render(request , 'index.html' ,{
                'result' : m,
                'form' : form
            })
    else:
        form =  MyForm()
        return render(request , 'index.html' , {'form' : form})
