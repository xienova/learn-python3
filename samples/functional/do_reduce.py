#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### 用reduce实现List中元素的连乘
from functools import reduce
def multi(x,y):
    return x*y
def prod(L):
    return reduce(multi,L)
print('3 * 5 * 7 * 9 = ',prod([3,5,7,9]))


###
from functools import reduce
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)         #map函数中用 lambda比较简洁
    point = 0
    def to_float(f, n):         # 在出现小数点后，运算规则发生了变化，用的判断条件 比较巧妙
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)          # 此处最后一个是 初始参数，有它时nums中的值 只能轮为第二参数

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
