from task6.forms import MyForm
from django.shortcuts import render



def singleNumber(request):
    x = 0
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        # assign variable
        if form.is_valid():
            x = form.cleaned_data['num']

    return render(request , 'index.html' , {'form' : form , 'result' : x})
