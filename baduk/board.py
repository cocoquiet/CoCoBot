# -*- coding: UTF-8 -*-

# import modules
try:
    import numpy as np
    import pandas as pd
    import math
except:
    raise ImportError("require the numpy,pandas,math module : please install the modules") # 모듈이 깔리지 않았을때 오류 발생

class Board():
    @classmethod
    def init_game_board(cls):
        cls.gameboard = pd.DataFrame([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],],
            index = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D"],
            columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D"],
        )
        return cls.gameboard

if __name__ == '__main__':
    board = Board()
    print(board.init_game_board())