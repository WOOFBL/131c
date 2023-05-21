import numpy as np
import pandas as pd

def numpytesting(lengs):
    a = np.eye(lengs,lengs)
    return a


def pandastest():
    table = pd.read_csv('myFile0.csv')
    df = pd.DataFrame([[1, 'Bob', 'Builder'],
                       [2, 'Sally', 'Baker'],
                       [3, 'Scott', 'Candle Stick Maker']],
                      columns=['id', 'name', 'occupation'])
    return 