#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):       # a代表起点， b代表缓冲点， c代表终点  a b c代表的意义在函数中不变， 且 各参数的位置 代表的 起点、终点不变
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)      #将上部的n-1个盘 从起点a 移到 缓冲点b
        move(1, a, b, c)        #将最底下的一个盘 从起点a 移动 终点c
        move(n-1, b, a, c)      #将n-1个盘 从缓冲区b 移动 终点c

move(4, 'A', 'B', 'C')
