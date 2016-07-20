from django.shortcuts import render
from django.http import HttpResponse


def mysum2(request, x):
    return HttpResponse(sum(int(i) for i in x.split('/')))

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))