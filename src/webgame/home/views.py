from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

import json

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))