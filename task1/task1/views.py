from django.http import HttpResponse
from django.shortcuts import render

def addxy(request):
    if(request.method == 'POST'):
        x =int(request.POST.get('num1'))
        y = int(request.POST.get('num2'))
        z =x+y

        # return HttpResponse("Result = " + str(z))
        return render(request , 'index.html' ,{
            'result' : str(z)
        })

    else:
        return render(request , 'index.html')