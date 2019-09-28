import random
from copy import deepcopy

from abc import ABCMeta, abstractmethod
from othello.backend.othello import OthelloSystem, BitBoard

class OthelloAI(metaclass=ABCMeta):

    def __init__(self, cpuColor, squares):
        self._cpuColor = cpuColor
        self._squares = squares
    
    @abstractmethod
    def think(self):
        raise NotImplementedError()

class RandomAI(OthelloAI):
    def __init__(self, cpuColor, squares):
        super().__init__(cpuColor, squares)

    def think(self):
        blackBoard, whiteBoard = BitBoard.squaresToBoard(self._squares)
        # 置く場所があるか判断．なければパスをする．
        if not ((self._cpuColor == OthelloSystem.BLACK and BitBoard.canPut(blackBoard, whiteBoard))
            or (self._cpuColor == OthelloSystem.WHITE and BitBoard.canPut(whiteBoard, blackBoard))):
            return None, None, None, None, None
        # ランダムに置いて最初にヒットしたところを選ぶ
        for idx in random.sample(range(64), k=64):
            x, y = BitBoard.calcXYfromInt(idx)
            print(idx, x, y)
            blackBoard_ret, whiteBoard_ret, history = OthelloSystem.putStone(deepcopy(blackBoard), deepcopy(whiteBoard), self._cpuColor, x, y)
            if blackBoard_ret is not None and whiteBoard_ret is not None:
                break
        return blackBoard_ret, whiteBoard_ret, x, y, history