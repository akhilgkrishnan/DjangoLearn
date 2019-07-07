from django.shortcuts import render
from django.http import HttpResponse
from .models import destination

# Create your views here.
def index(request):
    dest = destination()
    dest.id = 5
    dest.name = 'Akhil'
    dest.price = 500
    return render(request, "index.html",{'dest':dest}) #return the contents of index.html