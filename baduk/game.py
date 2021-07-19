# -*- coding: UTF-8 -*-

# import modules
try:
    import numpy as np
    import pandas as pd
    import math
    from board import Board  # 게임 보드와 관련된 기능들을 불러옵니다.
except Exception:
    raise ImportError("require the numpy,pandas,math module : please install the modules")  # 모듈이 깔리지 않았을때 오류 발생


class Baduk(Board):
    pass


if __name__ == '__main__':
    pass