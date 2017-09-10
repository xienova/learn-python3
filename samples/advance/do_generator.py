#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

    
# Fibonacci数列的定义与调用
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

        
# 杨辉三角
def triangles():
    L = [1,0]       # 此列表的末尾有 0 元素
    while True:
        yield L[:-1]        # 0 元素不让其显示，只显示前面的元素
        L = [1] + [L[x] + L[x-1] for x in range(1, len(L))] + [0]

n = 0
for t in triangles():
    print(t)
    n = n+1
    if n == 10:
        break
        
