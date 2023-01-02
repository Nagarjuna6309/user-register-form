from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse



def naga(request):
    uf=UserForm()
    pf=profileForm()
    d={'uf':uf,'pf':pf}
    if request.method=="POST":
        uf_data=UserForm(request.POST)
        pf_data=profileForm(request.POST)
        if uf_data.is_valid() and pf_data.is_valid():
            uf_data.save()
            pf_data.save()
            return HttpResponse('it is succesfulll..........................................')
    return render(request,'naga.html',d)