import random

from django.contrib.auth.models import User
from othello.models import Player, Status, Game, Chat

class DBControl(object):
    @staticmethod
    def createGameCPU(userId, cpuLevel):
        """ CPUとのゲームを新規作成
        
        Args:
            userId (int): ログインしているユーザーのID
            cpuLevel (int): 対戦するCPUのレベル
        
        Returns:
            othello.models.Game: 開始したゲームのインスタンス
        """
        # ユーザー取得
        user = User.objects.get(id=userId)
        # CPU情報取得
        cpuUser = User.objects.get(username="othello_cpu_{}".format(cpuLevel))
        cpu = Player.objects.get(user=cpuUser)
        # プレイヤー情報の作成or取得
        if len(Player.objects.filter(user=user)) == 0:
            player = Player(user=user)
            player.save()
        else:
            player = Player.objects.get(user=user)
        # ゲームステータスをonGameで作成
        status = Status.objects.get(status="onGame")
        # 以上のデータから新規ゲームを作成・保存
        game = Game(
            player1=player,
            player2=cpu,
            gameStatus=status,
            winner=None,
            firstPlayer="player{}".format(random.randint(1, 2)))
        game.save()
        # CPUからチャットを送る
        chat = Chat(game=game, speaker=cpuUser, message="Have a fun!")
        chat.save()
        return game

    @staticmethod
    def sendChat(gameId, userId, message):
        """ 送信されたチャットを保存する
        
        Args:
            gameId (int): 対戦中のゲームのID
            userId (int): 送信者のユーザID
            message (str): 送信されたメッセージ
        """
        game = Game.objects.get(id=gameId)
        user = User.objects.get(id=userId)
        chat = Chat(game=game, speaker=user, message=message)
        chat.save()

    @staticmethod
    def getChat(gameId):
        """ 特定のゲームのチャットをすべて取得する
        
        Args:
            gameId (int): 対戦中のゲームID
        
        Returns:
            list(str): メッセージ一覧
        """
        messages = []
        game = Game.objects.get(id=gameId)
        chats = Chat.objects.filter(game=game)
        for chat in reversed(chats):
            messages.append("[{}] {} ({})".format(chat.speaker, chat.message, str(chat.timestamp)[0:19]))
        return messages