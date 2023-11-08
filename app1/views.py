from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def viewfunc(request):
    return HttpResponse ('This is my 1st view function1')