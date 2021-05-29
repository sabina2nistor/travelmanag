from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import Travel

# Create your views here.

def index(request):
    travels = Travel.objects.all()
    return render(request,"mainapp/home.html",context={"travels":travels})


