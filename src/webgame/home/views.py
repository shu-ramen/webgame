from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

import json

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def sendData(request):
    print(request)
    if request.method == 'POST':
        response = json.dumps({'message' : "I recieved your message!!"})
        return HttpResponse(response, content_type="text/javascript")
    else:
        return Http404