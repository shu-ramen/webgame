import numpy as np

class OthelloSystem(object):
    EMPTY = -1
    BLACK = 0
    WHITE = 1

    @staticmethod
    def getInitSquares():
        """ 初期盤面を取得する

        Returns:
            list[list[int]]: オセロの盤面
        """
        blackBoard = 0x0000000810000000
        whiteBoard = 0x0000001008000000
        squares = BitBoard.boardToSquares(blackBoard, whiteBoard)
        return squares
    
    @staticmethod
    def putStone(blackBoard, whiteBoard, palyerColor, x, y):
        """ 石を置く
        
        Args:
            blackBoard (int): 黒のビットボード（64bit）
            whiteBoard (int): 白のビットボード（64bit）
            palyerColor (int): プレイヤーの石の色＝OthelloSystem.BLACK or OthelloSystem.WHITE
            x (int): 置き場所のX座標
            y (int): 置き場所のY座標
        
        Returns:
            int, int: 更新後の黒のビットボード，更新後の白のビットボード
        """
        pos = BitBoard.calcPos(x, y)
        legalBoard = None
        if palyerColor == OthelloSystem.BLACK:
            legalBoard = BitBoard.makeLegalBoard(blackBoard, whiteBoard)
        else:
            legalBoard = BitBoard.makeLegalBoard(whiteBoard, blackBoard)
        if pos & legalBoard:
            if palyerColor == OthelloSystem.BLACK:
                blackBoard, whiteBoard, reverseBoard, history = BitBoard.reverse(blackBoard, whiteBoard, pos)
            else:
                whiteBoard, blackBoard, reverseBoard, history = BitBoard.reverse(whiteBoard, blackBoard, pos)
        else:
            return None, None
        return blackBoard, whiteBoard, history

class BitBoard(object):
    VEC = [-9, -8, -7, -1, 1, 7, 8, 9]

    @staticmethod
    def squaresToBoard(squares):
        """ 盤面をリストからビットボードに変換する
        
        Args:
            squares (list[list[int]]): 盤面情報
        
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
            list[list[int]]: 盤面情報
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
        
    
    @staticmethod
    def countBoard(board):
        """ ボード上の石を数える
        
        Args:
            board (int): ビットボード（64bit）
        
        Returns:
            int: 石の数
        """
        count = 0
        mask = 0x8000000000000000
        for i in range(64):
            if mask & board:
                count = count + 1
            mask = mask >> 1
        return count

    @staticmethod
    def getIndices(board):
        """ 石の座標を取得
        
        Args:
            board (int): ビットボード（64bit）
        
        Returns:
            list[[int, int]]: 座標[x, y]のリスト
        """
        indices = []
        mask = 0x8000000000000000
        for i in range(64):
            if mask & board:
                indices.append([(i % 8), (i // 8)]) # [x, y]
            mask = mask >> 1
        return indices
    
    @staticmethod
    def makeLegalBoard(myBoard, enemyBoard):
        """ 合法手を作成
        
        Args:
            myBoard (int): 自色のビットボード（64bit）
            enemyBoard (int): 敵色のビットボード（64bit）
        
        Returns:
            int: 合法手のビットボード（64bit）
        """
        boardMask           =              0xffffffffffffffff     # 盤面を8x8に収めるマスク
        temp                =              0x0000000000000000     # 隣に相手の色があるかを一時保存
        legalBoard          =              0x0000000000000000     # 合法手ボード
        horizontalWatchMask = enemyBoard & 0x7e7e7e7e7e7e7e7e     # 敵コマを考慮した左右端の番人のマスク（左右の走査に使う）
        verticalWatchMask   = enemyBoard & 0x00ffffffffffff00     # 敵コマを考慮した上下端の番人のマスク（上下の走査に使う）
        allSideWatchMask    = enemyBoard & 0x007e7e7e7e7e7e00     # 敵コマを考慮した全辺の番人のマスク　（斜めの走査に使う）
        blankBoard          = ~(myBoard | enemyBoard) & boardMask # 空白を示すボード．空きは1．64bit（8x8）に収めている，

        # 左上                                     # 一つだけコメントを加えておく．
        temp = allSideWatchMask & (myBoard << 9)   # 自分の盤を左上にずらして敵駒がある限り追従する．はみ出したコマは消す．
        for i in range(5):                         # この操作を５回繰り返す．
            temp |= allSideWatchMask & (temp << 9) # ずらし操作
        legalBoard |= blankBoard & (temp << 9)     # もう一度ずらし操作を行い，敵駒を追跡した先が空いていれば置けるので，これは合法手となる．

        # 上
        temp = verticalWatchMask & (myBoard << 8)
        for i in range(5):
            temp |= verticalWatchMask & (temp << 8)
        legalBoard |= blankBoard & (temp << 8)

        # 右上
        temp = allSideWatchMask & (myBoard << 7)
        for i in range(5):
            temp |= allSideWatchMask & (temp << 7)
        legalBoard |= blankBoard & (temp << 7)

        # 左
        temp = horizontalWatchMask & (myBoard << 1)
        for i in range(5):
            temp |= horizontalWatchMask & (temp << 1)
        legalBoard |= blankBoard & (temp << 1)

        # 右
        temp = horizontalWatchMask & (myBoard >> 1)
        for i in range(5):
            temp |= horizontalWatchMask & (temp >> 1)
        legalBoard |= blankBoard & (temp >> 1)

        # 左下
        temp = allSideWatchMask & (myBoard >> 7)
        for i in range(5):
            temp |= allSideWatchMask & (temp >> 7)
        legalBoard |= blankBoard & (temp >> 7)

        # 下
        temp = verticalWatchMask & (myBoard >> 8)
        for i in range(5):
            temp |= verticalWatchMask & (temp >> 8)
        legalBoard |= blankBoard & (temp >> 8)

        # 右下
        temp = allSideWatchMask & (myBoard >> 9)
        for i in range(5):
            temp |= allSideWatchMask & (temp >> 9)
        legalBoard |= blankBoard & (temp >> 9)

        return legalBoard
    
    @staticmethod
    def calcPos(x, y):
        """ x, yからビットでの座標を計算
        
        Args:
            x (int): X座標
            y (int): Y座標
        
        Returns:
            int: ビットボードにおける座標（64bit）
        """
        pos = 0x8000000000000000
        for i in range(x + y * 8):
            pos = pos >> 1
        return pos
    
    
    @staticmethod
    def calcXY(pos):
        """ 64bit座標からXY座標を計算する
        
        Args:
            pos (int): 64bit座標
        
        Returns:
            int, int: X, Y座標
        """
        mask = 0x8000000000000000
        for i in range(64):
            if pos & mask:
                return (i % 8), (i // 8)
            pos = pos >> 1
        return -1, -1

    @staticmethod
    def reverse(myBoard, enemyBoard, putPos):
        """ 石を反転させる
        
        Args:
            myBoard (int): 自色のビットボード（64bit）
            enemyBoard (int): 敵色のビットボード（64bit）
            putPos (int): 石を置いた場所にフラグが立っている64bit整数
        
        Returns:
            int, int, int: 黒，白，反転箇所のビットボード（64bit）
        """
        history = []
        reverseBoard = 0x0000000000000000
        for vec in BitBoard.VEC:
            tempHistory = []
            tempBoard = 0x0000000000000000
            mask = BitBoard.transfer(putPos, vec) # posからvec方向に進む
            while ((mask != 0) and ((mask & enemyBoard) != 0)):
                # 範囲内にあり，捜査線上に敵コマが存在する限り繰り返す
                tempBoard |= mask
                tempHistory.append(BitBoard.calcXY(mask))
                mask = BitBoard.transfer(mask, vec)  # どんどんvec方向に進む
            if ((mask & myBoard) != 0):
                # 進んだ先に自コマがあればひっくり返す
                reverseBoard |= tempBoard
                history.extend(tempHistory)
        myBoard    ^= putPos | reverseBoard # 置いた駒と反転したコマの位置でXOR
        enemyBoard ^= reverseBoard          # 反転したコマの位置でXOR
        return myBoard, enemyBoard, reverseBoard, history
    
    def transfer(putPos, vec):
        """ vec方向にposを移動させる関数
        
        Args:
            putPos (int): 石を置いた場所にフラグが立っている64bit整数（移動後の可能性を含む）
            vec (int): 移動を示すベクトル（BitBoard.VEC）
        
        Returns:
            int: 移動後のpos
        """
        if (vec == -9): # 左上
            return (putPos << 9) & 0xfefefefefefefe00
        if (vec == -8): # 上
            return (putPos << 8) & 0xffffffffffffff00
        if (vec == -7): # 右上
            return (putPos << 7) & 0x7f7f7f7f7f7f7f00
        if (vec == -1): # 左
            return (putPos << 1) & 0xfefefefefefefefe
        if (vec == 1): # 右
            return (putPos >> 1) & 0x7f7f7f7f7f7f7f7f
        if (vec == 7): # 左下
            return (putPos >> 7) & 0x00fefefefefefefe
        if (vec == 8): # 下
            return (putPos >> 8) & 0x00ffffffffffffff
        if (vec == 9): # 右下
            return (putPos >> 9) & 0x007f7f7f7f7f7f7f
        return 0x0000000000000000
    
    @staticmethod
    def canPut(myBoard, enemyBoard):
        """ 配置可能性を調べる
        
        Args:
            myBoard (int): 自色のビットボード（64bit）
            enemyBoard (int): 敵色のビットボード（64bit）
        
        Returns:
            boolean: 配置可能性
        """
        myLegalBoard = BitBoard.makeLegalBoard(myBoard, enemyBoard)
        if myLegalBoard != 0:
            return True
        else:
            return False