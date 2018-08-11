# -*- coding:UTF8 -*-
#!/urs/bin/python
#队列相关
##########################################################################################
class Queue:
    '''队列的数据结构的实现
       列表首个元素位队尾'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop() 

class Queue1:
    '''队列的数据结构的实现
       列表首个元素位队首'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        item,self.items = self.items[0],self.items[1:]
        return item

class Deque:
    '''双队列的数据结构的实现
       列表首个元素为队尾'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


##########################################################################################
class PriorityQueue:
    '''优先级队列'''
    def __init__(self):
        self.heapArray   = [(0,0)]                 #占位，不使用,数据项从1开始
        self.currentSize =  0

    def __contains__(self,vtx):
        for pair in self.heapArray:
            if vtx == pair[1]:
                return True
        return False

    def buildHeap(self,Olist):
        '''利用列表构建新的干净的二叉堆
           时间复杂度:O(n)'''
        self.heapArray   = [(0,0)] + Olist[:]
        self.currentSize = len(Olist)
        size = len(Olist) >> 1 

        while size > 0:
            self.percDown(size)
            size -= 1

    def size(self):
        return self.currentSize

    def findMin(self):
        return self.heapArray[1]                   

    def isEmpty(self):
        return 0 == self.currentSize 


    #/************************1.插值函数相关函数开始*******************************/#
    def insert(self,pos):
        '''A:插值函数,添加到列表末尾'''
        self.heapArray.append(pos)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self,size):
        '''A的辅助函数:实现父子项交换'''
        while size >> 1 > 0:
            if self.heapArray[size][0] < self.heapArray[size >> 1][0]:
                tmp = self.heapArray[size >> 1]
                self.heapArray[size >> 1] = self.heapArray[size]
                self.heapArray[size] = tmp
            size >>= 1                        #*获取上一个父节点的位置*#
    #/*********************************1.END***************************************/#


    #/************************2.删除最小值函数相关函数开始**************************/#
    def delMin(self):
        '''B:删除最小项'''
        returnVal         = self.heapArray[1]   #*注意不是0*#
        self.heapArray[1] = self.heapArray.pop()
        self.currentSize -= 1
        self.percDown(1)                       #*从根向下交换父子项*#

        return returnVal
        
    def percDown(self,size):
        '''B的辅助函数1:实现父子项交换'''
        while (size << 1) < self.currentSize:
            minc = self.minChild(size)         #*返回子节点的最小位置*#
            if self.heapArray[size][0] > self.heapArray[minc][0]:
                tmp = self.heapArray[minc]
                self.heapArray[minc] = self.heapArray[size]
                self.heapArray[size] = tmp
            size = minc

    def minChild(self,size):
        '''B的辅助函数2:返回最小子项的位置'''
        if (size << 1) + 1 > self.currentSize: 
            #此时表示没有右子
            return size << 1
        elif self.heapArray[size << 1][0] < self.heapArray[(size << 1)+1][0]:
            #因为大的值尽量放在右边，所以判断用<,而非<=
            return size << 1  
        else:
            return (size << 1) + 1
    #/*********************************2.END***************************************/#


    def decreaseKey(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            

##########################################################################################
def hotPotato(namelist,num):
    '''利用队列做游戏'''
    queue = Queue()

    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()

def palchecker(aString):
    '''用双队列检查回文数字'''
    deque = Deque()

    for ch in aString:
        deque.addRear(ch)
    stillEqual = True 

    while deque.size() > 1 and  stillEqual:
        first = deque.removeFront()
        last  = deque.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual

