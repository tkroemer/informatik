from turtle import home
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Ferdinand Grasl bzw. Millena Tomic!")
