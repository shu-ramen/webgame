import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http.response import JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from othello.backend.DBControl import DBControl as DBC

# Create your views here.
@login_required
def index(request):
    template = loader.get_template('othello/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def vscpuHome(request, level):
    template = loader.get_template('othello/vscpu.html')
    context = {"isStarted": False}
    return HttpResponse(template.render(context, request))

@login_required
def vscpuCreate(request, level):
    print("Hi")
    if request.method == 'GET':
        game = DBC.createGameCPU(userId=request.user.id, cpuLevel=level)
        response = {"gameId": game.id}
        return JsonResponse(response)
    else:
        return Http404

@login_required
def vscpuShow(request, level, gameId):
    template = loader.get_template('othello/vscpu.html')
    context = {"isStarted": True}
    return HttpResponse(template.render(context, request))

@login_required
def vscpuSendChat(request, level, gameId):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        DBC.sendChat(gameId=gameId, userId=request.user.id, message=data["message"])
        response = {}
        return JsonResponse(response)
    else:
        return Http404

@login_required
def vscpuGetChat(request, level, gameId):
    if request.method == 'GET':
        messages = DBC.getChat(gameId=gameId)
        response = {"messages": messages}
        return JsonResponse(response)
    else:
        return Http404

@login_required
def vscpuGetBoard(request, level, gameId):
    if request.method == 'GET':
        squares, isMyTurn = DBC.getBoard(gameId=gameId, userId=request.user.id)
        response = {
            "squares": squares,
            "isMyTurn": isMyTurn
        }
        return JsonResponse(response)
    else:
        return Http404

@login_required
def vscpuPutStone(request, level, gameId):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        x = data["x"]
        y = data["y"]
        success, message = DBC.putStone(gameId=gameId, userId=request.user.id, x=x, y=y)
        if success:
            response = {
                "success": True
            }
        else:
            response = {
                "success": False,
                "message": message
            }
        return JsonResponse(response)
    else:
        return Http404