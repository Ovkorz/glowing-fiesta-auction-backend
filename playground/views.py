from django.shortcuts import render
from django.http import HttpResponse

def say_halp(request):
    x=1
    blabla = 'fdsdsafgd'
    return render(request, 'hello.html')

# Create your views here.
