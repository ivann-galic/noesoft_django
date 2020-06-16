from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('noesoft/index.html')
    return HttpResponse(template.render({}, request))