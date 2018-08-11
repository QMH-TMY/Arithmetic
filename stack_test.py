#-*- coding:UTF8 -*-
#!/usr/bin/python

class Stack():
    '''栈的数据结构的实现'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return [] == self.items

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


def parChecker1(parstr):
    '''检查括号是否匹配'''
    par   = parstr.split()
    leng  = len(par)
    index = 0
    stack = Stack()
    match = True

    while index < leng and match:
        token = par[index]
        if '(' == token:
            stack.push(token)
        elif ')' == token:
            if not stack.isEmpty():
                stack.pop()
            else:
                match = False
        else:
            pass
        index += 1

    if not stack.isEmpty():
        match = False

    return match

def matches(token1,token2):
    '''辅助检测函数'''
    str1 = '({['
    str2 = ')}]'
    return str1.index(token1) == str2.index(token2)

def parChecker2(parstr):
    '''检查各种括号是否匹配'''
    par   = parstr.split()
    leng  = len(par)
    index = 0
    stack = Stack()
    match = True

    while index < leng and match:
        token = par[index]
        if token in '({[':
            stack.push(token)
        elif token in ')}]':
            topToken = stack.peek()
            if not stack.isEmpty() and matches(topToken,token):
                stack.pop()
            else:
                match = False
        else:
            pass
        index += 1

    if not stack.isEmpty():
        match = False

    return match

def dec2bin(decNum,base=2):
    '''将十进制数转换位任意进制'''
    binNum = ""
    stack  = Stack()
    
    while decNum > 0:
        rem = decNum % base
        stack.push(rem)
        decNum /= base

    while not stack.isEmpty():
        binNum += str(stack.pop())
 
    return binNum

def infix2posfix(infixstr):
    '''制造后缀表达式'''
    hanstr = infixstr.split()
    stack  = Stack()
    output = []
    digits = "0123456789"
    alphbet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    par    = {}
    par['*'] = 3
    par['/'] = 3
    par['+'] = 2
    par['-'] = 2
    par['('] = 1

    for token in hanstr:
        if token in digits or token in alphbet:
            output.append(token)
        elif '(' == token:
            stack.push(token)
        elif ')' == token:
            topToken = stack.pop()
            if '(' != topToken:
                output.append(stack.pop())
                topToken = stack.pop()
        else:
            while not stack.isEmpty() and  pre[token] <= pre[stack.peek()]:
                output.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        output.append(stack.pop())

    return " ".join(output)

def caculate():
    '''辅助计算函数'''

def mathCaculate():
    '''计算后缀表达式 需用空格隔开'''
