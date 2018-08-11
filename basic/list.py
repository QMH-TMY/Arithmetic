# -*- coding:UTF8 -*-
#!/usr/bin/python
#列表
import time
import timeit

def sum1(n=10):
    '''计算1'''
    thesum=0
    for i in range(1,n+1):
        thesum += i
    return thesum

def sum2(n=10):
    '''计算2'''
    thesum = n*(1+n) / 2 

    return thesum

def sum3(n=10):
    '''计算3'''
    thesum = n*(1+n) >> 1

    return thesum

def arrage(s1,s2):
    '''计数和求乱序字符'''
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a') 
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a') 
        c2[pos] += 1
        
    i = 0
    stillok = True
    while i < 26 and stillok:
        if c1[i] == c2[i]:
            i += 1
        else:
            stillok = False
    return stillok

def testlist():
    '''构造列表'''
    l = []
    for i in range(1000):
        l += [i]                 #方法1
        l.append(i)              #方法2
    l = [i for i in range(1000)] #方法3
    l = list(range(1000))        #方法4


print"the sum is %d required %10.7f seconds"%sum1(10000)
print"the sum is %d required %10.7f seconds"%sum2(10000)
print"the sum is %d required %10.7f seconds"%sum3(10000)
t1 = Timer("testlist()","from __main__ import testlist")
print"concat ",t1.timeit(number=1000),"milliseconds")
#常见的列表操作函数的时间性能
index[]         O(1)
append[]        O(1)
pop()           O(1)
pop(i)          O(n)
insert(i,item)  O(n) 
del operator    O(n)
iteration       O(n)
contains(in)    O(n)
get slice [a:b] O(k)
del slice       O(n)
set slice       O(n+k)
reverse         O(n)
concatenate     O(k)
sort            O(nlogn)
multiply        O(n*k)

