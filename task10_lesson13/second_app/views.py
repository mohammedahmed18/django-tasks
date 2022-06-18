from django.shortcuts import render

# Create your views here.
def second(req):
    if req.method == 'GET':
        return render(req , 'second_app/index.html' , {'msg' : 'hello from the second app'})
