import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from collections import Iterator

pandas_head = {
    'HTML file': ['abs'],
    'author': 1,
    'author tag': 1,
    'author parent1 tag': 1,
    'author parent2 tag': 1,
    'author parent3 tag': 1,
    'author parent4 tag': 1,
    'author parent5 tag': 1,
    'content': 1,
    'content tag': 1,
    'content parent1 tag': 1,
    'content parent2 tag': 1,
    'content parent3 tag': 1,
    'content parent4 tag': 1,
    'content parent5 tag': 1,
}

index = sorted(pandas_head.keys())

def get_tag(tag):
    content = str(tag)
    formula = '^(<.*?>)'
    pattern = re.compile(formula)
    tag = re.findall(pattern, content)[0]
    return tag

def find_parent(parent):
    parent_tags = []
    for i in range(5):
        parent = parent.parent
        parent_tag = get_tag(parent)
        parent_tags.append(parent_tag)
    return (parent_tags)

def add_row(origin_dataframe, *datas):
    all  = []
    # print(origin_dataframe)
    # quit()
    for data in datas:
            all.append(data)
    series = pd.Series(all, index = index)
    # print(series)
    # s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
    # print(s2)
    # print(origin_dataframe)
    # print(origin_dataframe.append(series, ignore_index = True))
    # quit()
    return origin_dataframe.append(series, ignore_index = True)
