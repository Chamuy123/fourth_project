from django.shortcuts import render
from django.http import HttpResponse

def varma(request):
    return HttpResponse('<h1> <marquee>worth varma worth.....</h1></marquee>')
