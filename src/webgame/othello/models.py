from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.ForeignKey(User, related_name="player_user", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    winCount = models.IntegerField(default=0)
    loseCount = models.IntegerField(default=0)
    drawCount = models.IntegerField(default=0)

class Status(models.Model):
    status = models.CharField(max_length=16)

class Game(models.Model):
    player1 = models.ForeignKey("Player", related_name="game_player1", on_delete=models.SET_NULL, null=True)
    player2 = models.ForeignKey("Player", related_name="game_player2", on_delete=models.SET_NULL, null=True)
    gameStatus = models.ForeignKey("Status", related_name="game_gameStatus", on_delete=models.SET_NULL, null=True)
    winner = models.CharField(max_length=7, null=True)
    firstPlayer = models.CharField(max_length=7, null=True)
    lastUpdated = models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    game = models.ForeignKey("Game", related_name="log_game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", related_name="log_player", on_delete=models.SET_NULL, null=True)
    posX = models.IntegerField(null=False)
    posY = models.IntegerField(null=False)
    isPass = models.BooleanField(null=False)
    blackBoard = models.BigIntegerField(null=False)
    whiteBoard = models.BigIntegerField(null=False)
    timestamp = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    game = models.ForeignKey("Game", related_name="chat_game", on_delete=models.CASCADE)
    speaker = models.ForeignKey(User, related_name="chat_speaker", on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)