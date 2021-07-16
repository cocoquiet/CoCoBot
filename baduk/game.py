# -*- coding: UTF-8 -*-

# import modules
try:
    import numpy as np
    import pandas as pd
    import math
    from board import Board
except:
    raise ImportError("require the numpy,pandas,math module : please install the modules") # 모듈이 깔리지 않았을때 오류 발생


class Baduk(Board):
    pass