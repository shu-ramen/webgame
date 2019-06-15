import random

from django.contrib.auth.models import User
from othello.models import Player, Status, Game, Log, Chat
from othello.backend.othello import OthelloSystem, BitBoard
from othello.backend.AI import RandomAI

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
            list[str]: メッセージ一覧
        """
        messages = []
        game = Game.objects.get(id=gameId)
        chats = Chat.objects.filter(game=game)
        for chat in reversed(chats):
            messages.append("[{}] {} ({})".format(chat.speaker, chat.message, str(chat.timestamp)[0:19]))
        return messages
    
    @staticmethod
    def getBoard(gameId, userId):
        """ 最新の盤面と次のプレイヤー情報を取得
        
        Args:
            gameId (int): 対戦中のゲームID
            userId (int): ログイン中のユーザID
        
        Returns:
            list[list[int]], boolean: 盤面情報と次の指し手がユーザーか否か
        """
        # 変数を設定
        squares = None
        isMyTurn = False
        # ゲーム情報を取得
        game = Game.objects.get(id=gameId)
        # ログを取得
        logs = Log.objects.filter(game=game)
        if (len(logs) > 0):
            # 一つでも過去の指し手があれば，最新のログを取得
            log = logs.latest("timestamp")
            blackBoard = log.blackBoard
            whiteBoard = log.whiteBoard
            squares = BitBoard.boardToSquares(blackBoard, whiteBoard)
            if log.player.user.id != userId:
                isMyTurn = True
        else:
            # まだ一つも指し手がなければ，初期盤面と自分のターンかどうかを返す
            squares = OthelloSystem.getInitSquares()
            if game.firstPlayer == "player1":
                if game.player1.user.id == userId:
                    isMyTurn = True
            elif game.firstPlayer == "player2":
                if game.player2.user.id == userId:
                    isMyTurn = True
        # Return
        return squares, isMyTurn
    
    @staticmethod
    def putStone(gameId, userId, x, y):
        """ 石を置く
        
        Args:
            gameId (int): 対戦中のゲームID
            userId (int): ログイン中のユーザID
            x (int): X座標
            y (int): Y座標
        
        Returns:
            boolean, str: 石が置けたかどうかの真偽値，エラーメッセージ
        """
        squares, isMyTurn = DBControl.getBoard(gameId, userId)
        if isMyTurn == False:
            return False, "It's not your turn"
        playerColor = None
        game = Game.objects.get(id=gameId)
        player = Player.objects.get(user=User.objects.get(id=userId))
        if game.firstPlayer == "player1":
            if game.player1.user.id == userId:
                playerColor = OthelloSystem.BLACK
            else:
                playerColor = OthelloSystem.WHITE
        else:
            if game.player2.user.id == userId:
                playerColor = OthelloSystem.BLACK
            else:
                playerColor = OthelloSystem.WHITE
        blackBoard, whiteBoard = BitBoard.squaresToBoard(squares)
        blackBoard, whiteBoard, history = OthelloSystem.putStone(blackBoard, whiteBoard, playerColor, x, y)
        if blackBoard is not None and whiteBoard is not None:
            squares = BitBoard.boardToSquares(blackBoard, whiteBoard)
            log = Log(
                game=game,
                player=player,
                posX=x,
                posY=y,
                isPass=False,
                blackBoard=blackBoard,
                whiteBoard=whiteBoard
            )
            log.save()
            return True, "success"
        else:
            return False, "You cannot put there"
    
    @staticmethod
    def cpuPut(cpuLevel, gameId):
        """ CPUの手番実行
        
        Args:
            cpuLevel (int): CPUのレベル
            gameId (int): 対戦中のゲームID
        
        Returns:
            boolean, str: 石を置いたかどうかの真偽値，エラーメッセージ
        """
        # CPU情報取得
        cpuUser = User.objects.get(username="othello_cpu_{}".format(cpuLevel))
        cpu = Player.objects.get(user=cpuUser)
        squares, isCpuTurn = DBControl.getBoard(gameId, cpu.id)

        if isCpuTurn == False:
            return False, "It's not cpu's turn"
        game = Game.objects.get(id=gameId)
        if game.firstPlayer == "player1":
            if game.player1.user.id == cpu.id:
                cpuColor = OthelloSystem.BLACK
            else:
                cpuColor = OthelloSystem.WHITE
        else:
            if game.player2.user.id == cpu.id:
                cpuColor = OthelloSystem.BLACK
            else:
                cpuColor = OthelloSystem.WHITE
        if cpuLevel == 1:
            ai = RandomAI(cpuColor, squares)
        
        blackBoard, whiteBoard, x, y, history = ai.think()
        
        if (blackBoard is not None and whiteBoard is not None):
            log = Log(
                game=game,
                player=cpu,
                posX=x,
                posY=y,
                isPass=False,
                blackBoard=blackBoard,
                whiteBoard=whiteBoard
            )
            log.save()
            return True, "success"
        else:
            blackBoard, whiteBoard = BitBoard.squaresToBoard(squares)
            log = Log(
                game=game,
                player=cpu,
                posX=-1,
                posY=-1,
                isPass=True,
                blackBoard=blackBoard,
                whiteBoard=whiteBoard
            )
            log.save()
            return True, "success"