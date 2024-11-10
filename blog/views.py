from django.shortcuts import render
from .models import Telifon
def home(request):
    Telifon1 = Telifon.objects.all()
    return render(request,'index.html', {"Telifon": Telifon1})

def home1(request,id):
    Telifon1 = Telifon.objects.get(id=id)
    return render(request,'1.html',{"a": Telifon1})
