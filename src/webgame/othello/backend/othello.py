import numpy as np

class OthelloSystem(object):
    EMPTY = -1
    BLACK = 0
    WHITE = 1

    @staticmethod
    def getInitSquares():
        """ 初期盤面を取得する

        Returns:
            list(list(int)): オセロの盤面
        """
        blackBoard = 0x0000000810000000
        whiteBoard = 0x0000001008000000
        squares = BitBoard.boardToSquares(blackBoard, whiteBoard)
        return squares

class BitBoard(object):
    VEC = [-9, -8, -7, -1, 1, 7, 8, 9]

    @staticmethod
    def squaresToBoard(squares):
        """ 盤面をリストからビットボードに変換する
        
        Args:
            squares (list(list(int))): 盤面情報
        
        Returns:
            int, int: 黒のビットボード，白のビットボード
        """
        blackBoard = 0x0000000000000000
        whiteBoard = 0x0000000000000000
        mask       = 0x8000000000000000
        for i in range(8):
            for j in range(8):
                if squares[i][j] == OthelloSystem.BLACK:
                    blackBoard = blackBoard + mask
                if squares[i][j] == OthelloSystem.WHITE:
                    whiteBoard = whiteBoard + mask
                mask = mask >> 1
        return blackBoard, whiteBoard

    @staticmethod
    def boardToSquares(blackBoard, whiteBoard):
        """ 盤面をビットボードからリストに変換
        
        Args:
            blackBoard (int): 黒のビットボード（64bit整数）
            whiteBoard (int): 白のビットボード（64bit整数）
        
        Returns:
            list(list(int)): 盤面情報
        """
        squares = [[] for i in range(8)]
        mask = 0x8000000000000000
        for i in range(8):
            for j in range(8):
                if blackBoard & mask:
                    squares[i].append(OthelloSystem.BLACK)
                elif whiteBoard & mask:
                    squares[i].append(OthelloSystem.WHITE)
                else:
                    squares[i].append(OthelloSystem.EMPTY)
                mask = mask >> 1
        return squares