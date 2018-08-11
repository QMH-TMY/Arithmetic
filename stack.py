#-*- coding:UTF8 -*-
#!/usr/bin/python
#栈

class Stack:
    '''栈的数据结构实现'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
        #return self.items[len(self.items)-1]

def parChecker1(strings):
    '''检查括号是否匹配'''
    stack = Stack()
    index = 0
    match = True

    while index < len(strings) and match:
        symbol = strings[index] 
        
        if "(" == symbol:
            stack.push(symbol)
        elif ")" == symbol:
            if stack.isEmpty():
                match = False
            else:
                stack.pop()    
        else:
            pass

        index += 1

    if stack.isEmpty() and match:
        return True
    else:
        return False

def matches(op,cl):
    opens  = "({["
    closes = ")}]"
    return opens.index(op) == closes.index(cl)

def parChecker2(strings):
    '''检查各种括号是否匹配'''
    stack = Stack()
    index = 0
    match = True

    while index < len(strings) and match:
        symbol = strings[index] 
        
        if symbol in "({[":
            stack.push(symbol)
        elif symbol in ")}]":
            if stack.isEmpty():
                match = False
            else:
                top = stack.pop()    
                if not matches(top,symbol):
                    match = False
        else:
            pass

        index += 1

    if stack.isEmpty() and match:
        return True
    else:
        return False

def dec2bin(decNumber,base=2):
    '''将十进制数转换位2进制
       或者任意进制,只需把2
       换成对应的数字,例如8
       16等
    '''
    if not (1< base <= 16):
        print("Error base:correct base are from 2-16") 
        print("You can use the function in this way:")
        print("dec2bin(1024,16),dec2bin(1024,8)")
        exit(1)
        
    digits = "0123456789ABCDEF"
    stack = Stack()
    
    while decNumber > 0 :
        rem = decNumber % base 
        stack.push(rem)
        decNumber /= base

    binNumber = "" 
    while not stack.isEmpty():
        binNumber += digits[stack.pop()]


    return binNumber

def infix2posfix(infixstr):

    if not parChecker1(infixstr):
        print("Error,the str does not matched with ()")
        exit(1)

    pre = {}
    pre["*"] = 3
    pre["/"] = 3
    pre["+"] = 2
    pre["-"] = 2
    pre["("] = 1
    
    strlist = infixstr.split()
    output  = []
    stack   = Stack()
    alphbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits  = '0123456789' 

    for token in strlist:
        if token in alphbet or token in digits:
            output.append(token) 
        elif '('  == token:
            stack.push(token)
        elif ')'  == token:
            topToken = stack.pop()
            while '(' != topToken:
                output.append(topToken)
                topToken = stack.pop()
        else:
            while (not stack.isEmpty()) and (pre[token] <= pre[stack.peek()]):
                output.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        output.append(stack.pop())
    
    return " ".join(output) #用' '来链接列表项

def caculate(op,op1,op2):
    if "+" == op:
        return op1 + op2
    if "-" == op:
        return op1 - op2
    if "*" == op:
        return op1 * op2
    if "/" == op:
        return op1 / op2

def mathCaculate(infixstr):
    '''计算后缀表达式 需用空格隔开'''
    posfixstr = infix2posfix(infixstr)
    postToken = posfixstr.split() 

    postStack = Stack()
    digits    = '0123456789' 

    for token in postToken:
        if token in digits:
            postStack.push(int(token))
        else:
            op2 = postStack.pop()
            op1 = postStack.pop()
            res = caculate(token,op1,op2)
            postStack.push(res)

    return postStack.pop() 

print(infix2posfix("( 12 * 3 ) / 6"))
print(mathCaculate(" 12 3 * 6 /"))

