from django.shortcuts import render
from .models import Items

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the itemsImages index.")

def createImage(request, body):
    
    return HttpResponse()

def getImage(request, image_id):
    image = Items.objects.get(image_id)
    return HttpResponse({{image}})

def getAllImages(request, image_id):
    images_list = Items.objects.get()
    return HttpResponse({images_list})