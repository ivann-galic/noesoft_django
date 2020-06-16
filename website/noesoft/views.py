from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('noesoft/index.html')
    return HttpResponse(template.render({}, request))

def annonce_1(request):
    template = loader.get_template('noesoft/annonce_1.html')
    return HttpResponse(template.render({}, request))