# -*- coding:UTF8 -*-
#!/usr/bin/python
#搜索排序算法

#查找算法
def sequenSearch(Olist,item):
    '''乱序线性查找,时间复杂度:O(n)'''
    pos    = 0
    found  = False
    length = len(Olist)

    while pos < length and not found:
        if item == Olist[pos]:
            found = True
        else:
            pos  += 1

    return found


def OrdersequenSear(Olist,item):
    '''顺序线性查找,时间复杂度:O(n)'''
    pos   = 0
    found = False
    length  = len(Olist)
    #stop = False 加stop 可以得到另一版本的算法

    while pos < length and not found:
        if item == Olist[pos]:
            found = True
        elif item < Olist[pos]:
            return found
        else:
            pos  += 1

    return found

def binarySearch(Olist,item):
    '''二分查找,时间复杂度:O(log^n)'''
    '''排序有可能费时'''
    first = 0
    last  = len(Olist) - 1 
    found = False

    while first <= last and not found:
        midpos = (first + last) >> 1 
        if item == Olist[midpos]:
            found = True
        elif item < Olist[midpos]:
            last  = midpos -1
        else:
            first = midpos + 1

    return found
    

def binarySearch1(Olist,item):
    '''递归二分查找,时间复杂度:O(log^n)'''
    '''要考虑额外的列表切片时间
       排序有可能费时'''
    if 0 == len(Olist):
        return False
    else:
        midpos = len(Olist) >> 1
        if item == Olist[midpos]:
            return True
        elif item < Olist[midpos]:
            return binarySearch(Olist[:midpos],item)
        else:
            return binarySearch(Olist[midpos+1:],item)



def hashSearch(Olist,item):
    '''余数法哈希查找，时间复杂度O(1)'''
    '''列表必须符合哈希定义且没有冲突'''
    rem = item % len(Olist)
    if item == Olist[rem]:
        return True
    else:
        return False

#构造哈希散列函数的常见方法
#1.求余数
#2.分组求和(1,2)
#3.平方取中
#解决冲突的方法
#1.基于字符串的ascii值和
#2.构造槽的链
#3.移动到下一个或每次递增3的最近的槽


def hashCharfunc(astring,tablesize):
    '''解决冲突1：基于字符串的ascii值'''
    asum = 0
    for pos in range(len(astring)):
        asum += ord(astring[pos]) * pos

    return asum % tablesize


class HashTable:
    '''哈希表结构和查找,时间复杂度:O(1)'''
    def __init__(self,tablesize):
        self.size  = tablesize 
        self.slots = [None] * self.size
        self.datas = [None] * self.size

    def put(self,key,data):
        hval = self.hashfunc(key,len(self.slots))

        if self.slots[hval] == None:
            self.slots[hval] = key
            self.datas[hval] = data 
        else:
            if self.slots[hval] == key:
                self.datas[hval] = data 
            else:
                nhval = self.rehash(hval,len(self.slots))

                while self.slots[nhval] != None and self.slots[nhval] != key:
                    nhval = self.rehash(nhval,len(self.slots))

                if self.slots[nhval] == None:
                    self.slots[nhval] = key
                    self.datas[nhval] = data 
                else:
                    self.datas[nhval] = data 
                
    def hashfunc(self,key,size):
        return key % size

    def rehash(self,oldhash,size):
        return (oldhash + 1) % size

    def get(self,key):
        hval = self.hashfunc(key,len(self.slots))
        data = None
        stop = False
        found = False
        start = hval

        while self.slots[hval] != None and not found and not stop:
            if self.slots[hval] == key:
                found = True
                data  = self.datas[hval]
            else:
                hval  = rehash(hval,len(self.slots))
                if hval == start:
                    stop = True
        return data





#排序算法
def maopao(Olist):
    '''冒泡排序1,时间复杂度:O(n^2)'''
    length = len(Olist) - 1
    exchange = True #判断是否已排序 

    while length > 0 and exchange:
        exchange = False
        for i in range(length):
            if Olist[i] > Olist[i+1]:
                exchange,Olist[i],Olist[i+1] = True,Olist[i+1],Olist[i]

        length -= 1

def maopao1(Olist):
    '''冒泡排序2,时间复杂度:O(n^2)'''
    length = len(Olist) - 1
    exchange = length  #判断是否已排序

    while length > 0:
        for i in range(length):
            if Olist[i] > Olist[i+1]:
               Olist[i],Olist[i+1] = Olist[i+1],Olist[i]
            else:
                exchange -= 1

        if exchange == 0:
            print("Ordered List")
            return None

        length -= 1


def bubbleSort(Olist):
    '''冒泡排序3,时间复杂度:O(n^2)
       至少零次，至多n^2次交换'''
    length = len(Olist) - 1
    
    for times in range(length,0,-1):
        for i in range(times):
            if Olist[i] > Olist[i+1]:
                Olist[i],Olist[i+1] = Olist[i+1],Olist[i]


def selectionSort(Olist):
    '''选择排序1，时间复杂度O(n^2)
       至少至多n-1次交换'''
    length = len(Olist) - 1

    for curpos in range(length,0,-1):
        maxpos   = 0
        exchange = length #判断是否已排序
        for location in range(1,curpos+1):
            if Olist[location] > Olist[maxpos]:
                maxpos = location
                exchange -= 1 

        if 0 == exchange:
            print("Ordered List")
            return None

        Olist[maxpos],Olist[curpos] = Olist[curpos],Olist[maxpos]

def insertionSort(Olist):
    '''插入排序，事件复杂度O(n^2)'''
    length = len(Olist)

    for index in range(1,length):

        currVal = Olist[index]
        pos     = index

        while pos > 0 and Olist[pos-1] > currVal:
            Olist[pos] = Olist[pos-1]
            pos -= 1

        Olist[pos] = currVal


def shellSort(Olist):
    '''希尔排序，平均时间复杂度:O(n^3/2)'''
    gap = len(Olist) >> 1 #分割的子列表大小

    while gap > 0:
        for start in range(gap):
            gapInsertSort(Olist,start,gap)
        #print(gap,Olist) 查看列表和子列表大小
        gap >>= 1

def gapInsertSort(Olist,start,gap):
    '''增量插入排序'''

    for curpos in range(start+gap,len(Olist),gap):

        curVal = Olist[curpos]
        newpos = curpos

        while newpos >= gap and Olist[newpos-gap] > curVal:
            Olist[newpos] = Olist[newpos-gap]
            newpos -= gap 

        Olist[newpos] = curVal

def mergeSort(Olist):
    '''归并排序，利用递归，时间复杂度:O(nlog^n)
       迭代多，压榨深度需要考虑,大的列表不合适'''
    #print("Splitting",Olist)

    if len(Olist)> 1:
        midpos    = len(Olist) >> 1 
        leftside  = Olist[:midpos]
        rightside = Olist[midpos:]

        mergeSort(leftside)
        mergeSort(rightside)

        left,right,lst = 0,0,0
        while left < len(leftside) and right < len(rightside):
            if leftside[left] < rightside[right]:
                Olist[lst] =  leftside[left]
                left += 1
            else:
                Olist[lst] =  rightside[right]
                right += 1
            lst += 1

        while left < len(leftside):
            Olist[lst] = leftside[left]
            left += 1
            lst  += 1

        while right < len(rightside):
            Olist[lst] = rightside[right]
            right += 1
            lst   += 1
                

def quickSort(Olist):
    '''快速排序，时间复杂度:O(nlogn)-O(n^2)'''
    #first,last = firstpos(Olist)
    quickSortHelper(Olist,0,len(Olist)-1)

def firstpos(Olist):
    '''找最佳枢纽值'''
    length = len(Olist)
    helpli = [Olist[0],Olist[length >> 1],Olist[-1]]
    helpli.sort()

    if helpli[1] == Olist[0]:
        first = 0
    elif helpli[1] == Olist[-1]:
        first = length - 1
    else:
        first = length >> 1
    print(first,length-1)
    return first,length-1
    
def quickSortHelper(Olist,first,last):
    '''快速排序辅助函数，分区迭代'''
    if first < last:
        splitpos = partition(Olist,first,last)
        quickSortHelper(Olist,first,splitpos-1)
        quickSortHelper(Olist,splitpos+1,last)

def partition(Olist,first,last):
    '''快速排序分区函数'''
    pivotVal = Olist[first]

    left  = first + 1
    right = last
    done  = False

    while not done:
        while left <= right and Olist[left] <= pivotVal:
            left  += 1

        while left <= right and Olist[right] >= pivotVal:
            right -= 1

        if right < left:
            done = True
        else:
            Olist[left],Olist[right] = Olist[right],Olist[left]

    Olist[first],Olist[right] = Olist[right],Olist[first]
    
    return right


if __name__ == "__main__":
    #按照需要测试算法
    Olist = [31,26,93,17,54,20,44,55,77]
    quickSort(Olist)
    print(Olist)
