from task4.forms import MyForm
from django.http import HttpResponse
from django.shortcuts import render
def handleIsPrime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
def isPrime(request):
    if(request.method == 'POST'):
        form = MyForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num']
            prime = handleIsPrime(int(num))
            msg = 'the number is prime'
            if not prime:
                msg = 'the number is not prime'
        return render(request , 'index.html' ,{
            'result' : msg,
            'form' : form
        })

    else:
        form =  MyForm()
        return render(request , 'index.html' , {'form' : form})