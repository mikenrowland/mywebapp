from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world! I finally got my first web application using Django!! EUREKA!!!')
