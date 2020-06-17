from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from noesoft.models import Candidate

def home(request):
    template = loader.get_template('noesoft/index.html')
    return HttpResponse(template.render({}, request))

def annonce_1_confirmed(request, fname):
    template = loader.get_template('noesoft/annonce_1_confirmed.html')
    return HttpResponse(template.render({}, request))

def annonce_1(request):
    template = loader.get_template('noesoft/annonce_1.html')
    if request.method == 'POST':
        fname = request.POST.get('name')
        flast_name = request.POST.get('lastname')
        fmail = request.POST.get('mail')
        fphone = request.POST.get('phone')
        fmessage = request.POST.get('message')

        my_candidate = Candidate(name=fname, last_mane=flast_name, mail=fmail, phone=fphone, message=fmessage, job='test')
        my_candidate.save()
        return HttpResponseRedirect(reverse('annonce_1_confirmed', args=[fname]))

    # print(fname, flast_name, fmail, fphone, fmessage)
    return HttpResponse(template.render({}, request))

