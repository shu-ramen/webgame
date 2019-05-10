from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    template = loader.get_template('othello/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def vscpu(request, level):
    print(level)
    template = loader.get_template('othello/vscpu.html')
    context = {}
    return HttpResponse(template.render(context, request))