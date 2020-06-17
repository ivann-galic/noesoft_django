from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from noesoft.models import Candidate
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def home(request):
    template = loader.get_template('noesoft/index.html')
    return HttpResponse(template.render({}, request))

def annonce_1_confirmed(request, fname):
    template = loader.get_template('noesoft/annonce_1_confirmed.html')
    return HttpResponse(template.render({"candidate_name": fname}, request))

def annonce_1(request):
    template = loader.get_template('noesoft/annonce_1.html')
    if request.method == 'POST':
        fname = request.POST.get('name')
        flast_name = request.POST.get('lastname')
        fmail = request.POST.get('mail')
        fphone = request.POST.get('phone')
        ffile = request.FILES['myfile']
        file_name = default_storage.save(ffile.name, ffile)
        file_url = default_storage.url(file_name)

        fmessage = request.POST.get('message')

        my_candidate = Candidate(name=fname, last_mane=flast_name, mail=fmail, phone=fphone, file=file_url, message=fmessage, job='Alternance Développeur.se DJANGO')
        my_candidate.save()
        return HttpResponseRedirect(reverse('annonce_1_confirmed', args=[fname]))

    # print(fname, flast_name, fmail, fphone, fmessage)
    return HttpResponse(template.render({"job": "Alternance Développeur.se DJANGO"}, request))

