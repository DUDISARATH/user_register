from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

def registration(request):
    usfo=Userform()
    pfo=profileform()
    d={'usfo':usfo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        usfd=Userform(request.POST)
        pfd=profileform(request.POST,request.FILES)
        if usfd.is_valid() and pfd.is_valid():
            noot=usfd.save(commit=False)
            sp=usfd.cleaned_data['password']
            noot.set_password(sp)
            noot.save()
            poot=pfd.save(commit=False)
            poot.username=noot
            poot.save()
            send_mail('registration','registration is successfull','dudisarathroyal@gmail.com',[noot.email],fail_silently=False,
            )
            return HttpResponse('registration done')


    return render(request,'registration.html',d)