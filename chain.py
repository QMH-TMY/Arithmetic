# -*- coding:UTF8 -*-
#!/usr/bin/python
#链表，节点

class Node:
    '''链表的构造快：节点的数据结构'''
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext



class UnorderedList:
    '''无序链表的数据结构'''
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count   = 0
        
        while None != current:
            count  += 1
            current = current.getNext()

        return count 

    def search(self,item):
        current = self.head
        found   = False
        
        while None != current and not found:
            if item == current.getData():
                found = True
            else:
                current = current.getNext()

        return found 

    def pop(self,pos='N'):
        '''弹出元素'''
        current  = self.head
        previous = None

        if 'N' == pos:
            while None != current.getNext():
                previous = current
                current  = current.getNext()
            previous.setNext(current.getNext())
        else:
            if 0<= pos <= self.size():
                for i in range(pos):
                    previous = current
                    current  = current.getNext()
            else:
                print("Error number")
                exit(0)
            previous.setNext(current.getNext())

        return current.getData()
       
    def index(self,item):
        current = self.head
        found   = False
        count   = 0

        while None != current:
            if item == current.getData():
                return count
            else:
                previous = current
                current  = current.getNext()
                count   += 1

        print("%s do not exist"%item) 
        
    def add(self,item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node
    
    def append(self,item):
        current  = self.head
        previous = None
        node = Node(item)

        if None == self.head:
            self.head = node
        else:
            while None != current:
                previous = current
                current  = current.getNext()

        previous.setNext(node)

    def insert(self,pos,item):
        current  = self.head
        previous = None

        for i in range(pos):
            previous = current
            current  = current.getNext()

        node = Node(item)
        node.setNext(current)
        previous.setNext(node)

    def remove(self,item):
        current  = self.head
        previous = None
        found    = False

        while previous != current and not found:
            if item == current.getData():
                found = True
            else:
                previous = current
                current  = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class OrderedList:
    '''有序链表的数据结构'''
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count   = 0

        while None != current:
            count  += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found   = False
        
        while None != current and not found:
            if item == current.getData():
                found = True
            elif item > current.getData():
                current = current.getNext()
            else:
                current = None

        return found 

    def pop(self,pos='N'):
        current  = self.head
        previous = None

        if 'N' == pos:
            while None != current.getNext():
                previous = current
                current  = current.getNext()

            previous.setNext(current.getNext())
        else:
            if 0<= pos <= self.size():
                for i in range(pos):
                    previous = current
                    current  = current.getNext()
            else:
                print("Error number")
            previous.setNext(current.getNext())

        return current.getData()
       
    def index(self,item):
        current = self.head
        found   = False
        count   = 0

        while None != current:
            if item == current.getData():
                return count
            else:
                previous = current
                current  = current.getNext()
                count   += 1

        print("%s do not exist"%item) 
        
    def add(self,item):
        current  = self.head
        previous = None
        stop     = False

        while None != current and not stop:
            if item < current.getData():
                stop = True
            else:
                previous = current
                current  = current.getNext()

        node = Node(item)
        if previous == None:
            node.setNext(self.head)
            self.head = node
        else:
            node.setNext(current)
            previous.setNext(node)
    
    def append(self,item):
        current  = self.head
        previous = None
        node = Node(item)

        if None == self.head:
            self.head = node
        else:
            while None != current:
                previous = current
                current  = current.getNext()

        previous.setNext(node)

    def insert(self,pos,item):
        current  = self.head
        previous = None

        for i in range(pos):
            previous = current
            current  = current.getNext()

        node = Node(item)
        node.setNext(current.getNext())
        previous.setNext(node)

    def remove(self,item):
        current  = self.head
        previous = None
        found    = False

        while previous != current and not found:
            if item == current.getData():
                found = True
            else:
                previous = current
                current  = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

