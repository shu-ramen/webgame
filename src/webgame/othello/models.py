from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    """ othello_player：プレイヤー情報

    Args:
        user (django.contrib.auth.models.User): ユーザー情報
        rating (models.IntegerField): レート（default=0）
        winCount (models.IntegerField): 勝ち数（default=0)
        loseCount (models.IntegerField): 負け数（default=0）
    """
    user = models.ForeignKey(User, related_name="player_user", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    winCount = models.IntegerField(default=0)
    loseCount = models.IntegerField(default=0)
    drawCount = models.IntegerField(default=0)

class Status(models.Model):
    """ othello_status：対局状況
    
    Args:
        status (models.CharField): 対局状況を示す文字列（max_length=16）
    """
    status = models.CharField(max_length=16)

class Game(models.Model):
    """ othello_game：ゲーム情報
    
    Args:
        player1 (othello.models.Player): プレイヤー１の情報
        player2 (othello.models.Player): プレイヤー２の情報
        gameStatus (othello.models.Status): 対局状況
        winner (models.CharField): "player1" or "player2" or null
        firstPlayer (models.CharField): "player1" or "player2" or null
        lastUpdated (models.DateTimeField): 最終更新時のタイムスタンプ（auto_now_add=True）
    """
    player1 = models.ForeignKey("Player", related_name="game_player1", on_delete=models.SET_NULL, null=True)
    player2 = models.ForeignKey("Player", related_name="game_player2", on_delete=models.SET_NULL, null=True)
    gameStatus = models.ForeignKey("Status", related_name="game_gameStatus", on_delete=models.SET_NULL, null=True)
    winner = models.CharField(max_length=7, null=True)
    firstPlayer = models.CharField(max_length=7, null=True)
    lastUpdated = models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    """ othello_log：棋譜
    
    Args:
        game (othello.models.Game): ゲーム情報
        player (othello.models.Player): 指し手のプレイヤーの情報
        posX (models.IntegerFiled): X座標（0~7 or -1）
        posY (models.IntegerFiled): Y座標（0~7 or -1）
        isPass (models.BooleanField): パスかどうか
        blackBoard (models.BigIntegerField): 黒のビットボード（64bit）
        whiteBoard (models.BigIntegerField): 白のビットボード（64bit）
        timestamp (models.DateTimeField): 棋譜追加時のタイムスタンプ（auto_now=True）
    """
    game = models.ForeignKey("Game", related_name="log_game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", related_name="log_player", on_delete=models.SET_NULL, null=True)
    posX = models.IntegerField(null=False)
    posY = models.IntegerField(null=False)
    isPass = models.BooleanField(null=False)
    blackBoard = models.BigIntegerField(null=False)
    whiteBoard = models.BigIntegerField(null=False)
    timestamp = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    """ othello_chat：チャット
    
    Args:
        game (othello.models.Game): ゲーム情報
        speaker (django.contrib.auth.models.User): 発言者のユーザー情報
        message (models.CharField): 発言内容（max_length=256）
        timestamp (models.DateTimeField): 発言時のタイムスタンプ（auto_now=True）
    """
    game = models.ForeignKey("Game", related_name="chat_game", on_delete=models.CASCADE)
    speaker = models.ForeignKey(User, related_name="chat_speaker", on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)