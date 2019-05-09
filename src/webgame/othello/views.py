from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('othello/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def vscpu(request, level):
    print(level)
    template = loader.get_template('othello/vscpu.html')
    context = {}
    return HttpResponse(template.render(context, request))