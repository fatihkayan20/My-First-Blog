from django.shortcuts import *

# Create your views here.

def index(request):
    return HttpResponse("Merhaba Django")

