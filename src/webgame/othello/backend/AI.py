import random

from abc import ABCMeta, abstractmethod
from othello.backend.othello import OthelloSystem, BitBoard

class OthelloAI(metaclass=ABCMeta):

    def __init__(self, cpuColor, squares):
        self._cpuColor = cpuColor
        self._squares = squares

    @property
    def cpuColor(self):
        return self._cpuColor
    
    @property
    def squares(self):
        return self._squares
    
    @abstractmethod
    def think(self):
        raise NotImplementedError()

class RandomAI(OthelloAI):
    def __init__(self, cpuColor, squares):
        super().__init__(cpuColor, squares)

    def think(self):
        blackBoard, whiteBoard = BitBoard.squaresToBoard(self.squares)
        # 置く場所があるか判断．なければパスをする．
        for i in range(64):
            if self.cpuColor == OthelloSystem.BLACK and BitBoard.canPut(blackBoard, whiteBoard):
                break
            elif self.cpuColor == OthelloSystem.WHITE and BitBoard.canPut(whiteBoard, blackBoard):
                break
            if i == 63:
                return None, None
        # ランダムに置いて最初にヒットしたところを選ぶ
        myBoard = None
        enemyBoard = None
        reverseBoard = None
        history = None
        while (True):
            idx = random.randrange(64)
            pos = 0x8000000000000000
            for i in range(idx):
                pos = pos >> 1
            if self.cpuColor == OthelloSystem.BLACK:
                myBoard, enemyBoard, reverseBoard, history = BitBoard.reverse(blackBoard, whiteBoard, pos)
            elif self.cpuColor == OthelloSystem.WHITE:
                myBoard, enemyBoard, reverseBoard, history = BitBoard.reverse(whiteBoard, blackBoard, pos)
            if BitBoard.countBoard(reverseBoard):
                x, y = BitBoard.calcXY(pos)
                break
        return myBoard, enemyBoard, x, y, history