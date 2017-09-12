#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 将用户输入的不规范英文名字，变为 首字母大写，其他小写的 规范名字。
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
