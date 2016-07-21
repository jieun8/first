from django.shortcuts import render
from pockemon.models import Pockemon

def pockemon_list(request):
    qs = Pockemon.objects.all()
    return render(request, "pockemon_list.html",
        {'pockemon_list': qs})