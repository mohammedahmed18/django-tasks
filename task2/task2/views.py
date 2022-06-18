from task2.forms import AddForm
from django.http import HttpResponse
from django.shortcuts import render

def addFunc(request):
    if(request.method == 'POST'):
        form = AddForm(request.POST)
        if form.is_valid():
           x = form.cleaned_data['first_number']
           y = form.cleaned_data['second_number']
           result = x + y
        # return HttpResponse("Result = " + str(z))
        return render(request , 'index.html' ,{
            'result' : str(result),
            'form' : form
        })

    else:
        form =  AddForm()
        return render(request , 'index.html' , {'form' : form})