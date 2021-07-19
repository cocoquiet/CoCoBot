# -*- coding: UTF-8 -*-

# import modules
try:
    import numpy as np
    import pandas as pd
    import math
except Exception: # 모든 예외를 잡습니다. (보나마나 import 에러밖에 없겠지만...)
    raise ImportError("require the numpy,pandas,math module : please install the modules")  # 모듈이 깔리지 않았을때 오류 발생


class Board:
    gameboard = None
    @classmethod
    def init_game_board(cls):
        """
        게임에 사용될 게임보드를 Dataframe 형태로 변환하여 저장합니다.
        이 메소드는 게임보드 초기화, 게임보드 생성 이 두 기능 모두 사용할수 있습니다.
        이 게임보드는 13 x 13 크기로 이루어져 있습니다.
        :return gameboard:
        """
        Board.gameboard = pd.DataFrame([
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ],  # 13 x 13 배열의 리스트를 생성합니다.
            index=[1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D"],  # 세로테그를 수정합니다.
            columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D"]  # 가로테그를 수정합니다.
        )
        return Board.gameboard

    @classmethod
    def add_the_white_stone(cls, x_coordinate, y_coordinate):
        Board.gameboard.loc[x_coordinate, y_coordinate] = "W"
        return Board.gameboard


if __name__ == '__main__':
    board = Board()
    print(board.init_game_board())
    print(Board.add_the_white_stone(2,2))