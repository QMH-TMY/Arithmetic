# -*- coding:UTF8 -*-
#!/usr/bin/python
#Shieber on 2018/8/7
#树,二叉堆的结构

######################################################## 
#树的实现方法一:列表
def BinaryTree1(tree):
    '''二叉树的实现'''
    return [tree,[],[]]

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def insertLeft(root,newBranch):
    '''加入左树'''
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    '''加入右树'''
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

#树的实现方法二:节点和引用
class BinaryTree2:
    '''二叉树的实现'''
    def __init__(self,root):
        self.root       = root
        self.leftChild  = None
        self.rightChild = None
    
    def getRootVal(self):
        return self.root

    def setRootVal(self,Obj):
        self.root = Obj 

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def preorder(self):
        '''前序遍历,内部实现:中左右'''
        print(self.root)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def midorder(self):
        '''中序遍历,内部实现:右中左'''
        if self.rightChild:
            self.rightChild.midorder()
        print(self.root)
        if self.leftChild:
            self.leftChild.midorder()

    def postorder(self):
        '''后序遍历,内部实现:右左中'''
        if self.rightChild:
            self.rightChild.postorder()
        if self.leftChild:
            self.leftChild.postorder()
        print(self.root)

    def insertLeft(self,newBranch):
        if None == self.leftChild:
            self.leftChild = BinaryTree(newBranch)
        else:
            t = BinaryTree(newBranch)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newBranch):
        if None == self.rightChild:
            self.rightChild = BinaryTree(newBranch)
        else:
            t = BinaryTree(newBranch)
            t.rightChild = self.rightChild
            self.rightChild = t

def preorder(tree):
    '''前序遍历,外部实现'''
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def midorder(tree):
    '''中序遍历,外部实现'''
    if tree:
        midorder(tree.getLeftChild())
        print(tree.getRootVal())
        midorder(tree.getRightChild())

def midorder1(tree):
    '''中序遍历,加上括号,外部实现'''
    sVal = ''
    if tree:
        sVal = '(' + midorder1(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + midorder1(tree.getRightChild()) + ')'
    return sVal

def postorder(tree):
    '''后序遍历,外部实现'''
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

####################################################################
#from pythonds.basic.stack import Stack 

def analiTree(string):
    '''计算式分析树,利用了栈'''
    strlist = string.split()
    stack   = Stack()
    tree    = BinaryTree('')

    stack.push(tree)
    currTree = tree
    
    for token in strlist:
        if '(' == token:
            currTree.insertLeft('')
            stack.push(currTree)
            currTree = currTree.getLeftChild()
        elif token not in ['+','-','*','/',')']:
            currTree.setRootVal(int(token))
            currTree = stack.pop()
        elif token in ['+','-','*','/']:
            currTree.setRootVal(token)
            currTree.insertRight('')
            stack.push(currTree)
            currTree = currTree.getRightChild()
        elif ')' == token:
            currTree = stack.pop()
        else:
            raise ValueError

    return tree

def evaluate(tree):
    '''计算分析树的评估函数'''
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

    left  = tree.getLeftChild()
    right = tree.getRightChild()

    if left and right:
        func = opers[tree.getRootVal()]
        return func(evaluat(left),evaluate(right))
    else:
        return tree.getRootVal()
def postorderEval(tree):
    '''后序遍历的评估函数'''
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1,res1 = None,None

    if tree:
        res1 = postorderEval(tree.getLeftChild())
        res2 = postorderEval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

############################################################################
#二叉堆类
class BinHeap:
    '''二叉堆的实现,可用于优先级队列的创建'''
    def __init__(self):
        self.heapList    = [0]                 #占位，不使用,数据项从1开始
        self.currentSize =  0

    def findMin(self):
        return self.heapList[1]

    def size(self):
        return self.currentSize

    def isEmpty(self):
        return 0 == self.currentSize 

    #/************************1.插值函数相关函数开始*******************************/#
    def insert(self,pos):
        '''A:插值函数,添加到列表末尾'''
        self.heapList.append(pos)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self,size):
        '''A的辅助函数:实现父子项交换'''
        while size >> 1 > 0:
            if self.heapList[size] < self.heapList[size >> 1]:
                tmp = self.heapList[size >> 1]
                self.heapList[size >> 1] = self.heapList[size]
                self.heapList[size] = tmp
            size >>= 1                        #*获取上一个父节点的位置*#
    #/************************1.插值函数相关函数结束*******************************/#


    #/************************2.删除最小值函数相关函数开始**************************/#
    def delMin(self):
        '''B:删除最小项'''
        returnVal         = self.heapList[1]   #*注意不是0*#
        self.heapList[1]  = self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)                       #*从根向下交换父子项*#

        return returnVal
        
    def percDown(self,size):
        '''B的辅助函数1:实现父子项交换'''
        while size << 1 < self.currentSize:
            minc = self.minChild(size)         #*返回子节点的最小位置*#
            if self.heapList[size] > self.heapList[minc]:
                tmp = self.heapList[minc]
                self.heapList[minc] = self.heapList[size]
                self.heapList[size] = tmp
            size = minc

    def minChild(self,size):
        '''B的辅助函数2:返回最小子项的位置'''
        if (size << 1) + 1 > self.currentSize: 
            #此时表示没有右子
            return size << 1
        elif self.heapList[size << 1] < self.heapList[(size << 1)+1]:
            #因为大的值尽量放在右边，所以判断用<,而非<=
            return size << 1  
        else:
            return (size << 1) + 1
    #/************************2.删除最小值函数相关函数结束**************************/#


    def buildHeap(self,Olist):
        '''利用列表构建新的干净的二叉堆
           时间复杂度:O(n)'''
        self.heapList    = [0] + Olist[:]
        self.currentSize = len(Olist)
        size = len(Olist) >> 1 

        while size > 0:
            self.percDown(size)
            size -= 1
        
############################################################################
class TreeNode:
    '''树节点'''
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key        = key
        self.payload    = val
        self.leftChild  = left
        self.rightChild = right
        self.parent     = parent
        #self.balFactor = 0

    def __iter__(self):
        '''迭代生产器yield'''
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild():
                    yield elem

            yield self.key

            if self.hasRightChild():
                for elem in self.rightChild():
                    yield elem
            
    def hasChild(self):
        return self.leftChild or self.rightChild
        
    def has2Child(self):
        return self.leftChild and self.rightChild

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild  == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightchild)

    def replaceNodeData(self,key,val,leftC,rightC):
        self.key        = key
        self.payload    = val
        self.leftChild  = leftC
        self.rightChild = rightC

        if self.hasLeftChild():
            self.leftChild  = self

        if self.hasRightChild():
            self.rightChild = self


class BinarySearchTree:
    '''二叉搜索树'''
    def __init__(self):
        self.root = None
        self.size = 0 

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    #/*************1.创建二叉搜索树的相关函数开始****************/# 
    def __setitem__(self,key,val):
        '''重新赋值[],实现
        myTree['key'] = val操作'''
        self.put(key,val)

    def put(self,key,val):
        '''创建二叉搜索树'''
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val) #引用树节点类 
        self.size += 1

    def _put(self,key,val,currNode):
        '''创建二叉搜索树迭代判断函数'''
        #key == currNode.key 需要考虑吗？
        if key < currNode.key:
            if currNode.hasLeftChild():
                self._put(key,val,currNode.leftChild)
            else:
                currNode.leftChild  = TreeNode(key,val,parent=currNode)
        else:
            if currNode.hasRightChild():
                self._put(key,val,currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(key,val,parent=currNode)
    #/*************1.创建二叉搜索树的相关函数结束****************/# 


    #/*************2.获取二叉搜索树数据的相关函数开始****************/# 
    def __getitem__(self,key):
        '''重新赋值[],实现
           val = myTree['key']操作'''
        return self.get(key)

    def get(self,key):
        '''获取二叉搜索树数据'''
        if self.root:
            data = self._get(key,self.root)
            if data:
                return data.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currNode):
        '''获取二叉树数据迭代判断函数'''
        if not currNode.key:
            return None
        elif key == currNode.key:
            return currNode
        elif key <  currNode.key:
            return self._get(key,currNode.leftChild)
        else:
            return self._get(key,currNode.rightChild)

    def __contains__(self,key):
        '''重载in函数'''
        if self._get(key,self.root):
            return True
        else:
            return False 
    #/*************2.获取二叉搜索树数据的相关函数结束****************/# 


    #/*************3.删除二叉搜索树节点的相关函数开始****************/# 
    def __delitem__(self,key):
        self.delete(key)

    def delete(self,key):
        '''删除键'''
        if self.size > 1:
            node2Remove = self._get(key,self.root)
            if node2Remove:
                self.remove(node2Remove)
                self.size -= 1
            else:
                raise KeyError('Error,key does not exist')
        elif 1 == self.size and key == self.root.key:
            self.root  = None
            self.size -= 1
        else:
            raise KeyError('Error,key does not exist')

    def remove(self,node):
        '''删除键,维持树的平恒'''
        if node.isLeaf():     #叶节点　
            if node == node.parent.leftChild:
                node.parent.leftChild  = None
            else:
                node.parent.rightChild = None
        elif node.has2Child():#父节点，两个孩子
            succ = node.findSuccessor()
            succ.spliceOut()
            node.key     = succ.key
            node.payload = succ.payload
        else:                 #父节点，一个孩子 六种情况
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.leftChild.parent = node.parent
                    node.patent.leftChild = node.leftChild
                elif node.isRightChild():
                    node.leftChild.parent  = node.parent
                    node.patent.rightChild = node.leftChild
                else:
                    node.replaceNodeData(node.leftChild.key,
                                         node.leftChild.payload,
                                         node.leftChild.leftChild,
                                         node.leftChild.rightChild)
            else:
                if node.isLeftChild():
                    node.rightChild.parent = node.parent
                    node.patent.leftChild  = node.rightChild
                elif node.isRightChild():
                    node.rightChild.parent = node.parent
                    node.patent.rightChild = node.rightChild
                else:
                    node.replaceNodeData(node.rightChild.key,
                                         node.rightChild.payload,
                                         node.rightChild.leftChild,
                                         node.rightChild.rightChild)
    def findSuccessor(self):
        '''找到后继节点，在右子树的最小左子树位置'''
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin() 
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        '''找到最小左子树'''
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        '''删除后继节点'''
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild  = None 
            else:
                self.parent.rightChild = None 
        elif self.hasChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild  = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent      = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild  = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent     = self.parent
        else:
            pass
    #/*************3.删除二叉搜索树节点的相关函数结束****************/# 
#mytree = BinarySearchTree()
#mytree[3] = 'red'
#mytree[4] = 'blue'
#mytree[6] = 'yellow'
#print(mytree[])
#print(mytree[3])

############################################################################
#平衡二叉搜索树AVL
#平衡因子:height(leftTree) - height(rightTree)
#N=O^(h+2)/sqrt(5) -1 树节点
#h=1.44*logNh         树高
class BinarySearchTreeAVL:
    '''平衡二叉搜索树,只需要稍微
       改变一下二叉搜索树的一些
       函数,限制搜索为O(logn)'''
    def __init__(self):
        self.root = None
        self.size = 0 

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    #/*************1.创建平衡二叉搜索树的相关函数开始****************/# 
    def __setitem__(self,key,val):
        '''重新赋值[],实现
        myTree['key'] = val操作'''
        self.put(key,val)

    def put(self,key,val):
        '''创建二叉搜索树'''
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val) #引用树节点类 
        self.size += 1

    def _put(self,key,val,currNode):
        '''创建二叉搜索树迭代判断函数'''
        #key == currNode.key 需要考虑吗？
        if key < currNode.key:
            if currNode.hasLeftChild():
                self._put(key,val,currNode.leftChild)
            else:
                currNode.leftChild  = TreeNode(key,val,parent=currNode)
                self.updateBalance(currNode.leftChild)
        else:
            if currNode.hasRightChild():
                self._put(key,val,currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(key,val,parent=currNode)
                self.updateBalance(currNode.rightChild)

    def updateBalance(self,node):
        '''每次插入数据项时,实现树的平衡'''
        if node.balFactor > 1 or node.balFactor < -1:
            self.rebalance(node)
            return True 
        if node.parent:
            if node.isLeftChild():
                node.parent.balFactor += 1
            elif node.isRightChild():
                node.parent.balFactor -= 1
            else:
                pass

            if node.parent.balFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self,node):
        '''调整极端情况'''
        if  node.balFactor < 0:
            if node.rightChild.balFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balFactor >0:
            if node.leftChild.balFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
        else:
            pass
            
    def rotateLeft(self,rotRoot):
        '''子树左旋转'''
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild

        if None != newRoot.leftChild:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent

        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild  = newRoot
            else:
                rotRoot.parent.rightChild = newRoot

        newRoot.leftChild = rotRoot         
        rotRoot.parent    = newRoot
        rotRoot.balFactor = rotRoot.balFactor + 1 - min(newRoot.balFactor,0)
        newRoot.balFactor = newRoot.balFactor + 1 + max(rotRoot.balFactor,0)

    def rotateRight(self,rotnode):
        '''子树右旋转'''
       newRoot = rotRoot.leftChild
       rotRoot.leftChild = newRoot.rightChild

        if None != newRoot.rightChild:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent

        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild  = newRoot

        newRoot.rightChild = rotRoot         
        rotRoot.parent     = newRoot
        rotRoot.balFactor  = rotRoot.balFactor - 1 - max(newRoot.balFactor,0)
        newRoot.balFactor  = newRoot.balFactor - 1 + min(rotRoot.balFactor,0)

    #/*************1.创建平衡二叉搜索树的相关函数结束****************/# 


    #/*************2.获取二叉搜索树数据的相关函数开始****************/# 
    def __getitem__(self,key):
        '''重新赋值[],实现
           val = myTree['key']操作'''
        return self.get(key)

    def get(self,key):
        '''获取二叉搜索树数据'''
        if self.root:
            data = self._get(key,self.root)
            if data:
                return data.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currNode):
        '''获取二叉树数据迭代判断函数'''
        if not currNode.key:
            return None
        elif key == currNode.key:
            return currNode
        elif key <  currNode.key:
            return self._get(key,currNode.leftChild)
        else:
            return self._get(key,currNode.rightChild)

    def __contains__(self,key):
        '''重载in函数'''
        if self._get(key,self.root):
            return True
        else:
            return False 
    #/*************2.获取二叉搜索树数据的相关函数结束****************/# 


    #/*************3.删除二叉搜索树节点的相关函数开始****************/# 
    def __delitem__(self,key):
        self.delete(key)

    def delete(self,key):
        '''删除键'''
        if self.size > 1:
            node2Remove = self._get(key,self.root)
            if node2Remove:
                self.remove(node2Remove)
                self.size -= 1
            else:
                raise KeyError('Error,key does not exist')
        elif 1 == self.size and key == self.root.key:
            self.root  = None
            self.size -= 1
        else:
            raise KeyError('Error,key does not exist')

    def remove(self,node):
        '''删除键,维持树的平恒'''
        if node.isLeaf():     #叶节点　
            if node == node.parent.leftChild:
                node.parent.leftChild  = None
            else:
                node.parent.rightChild = None
        elif node.has2Child():#父节点，两个孩子
            succ = node.findSuccessor()
            succ.spliceOut()
            node.key     = succ.key
            node.payload = succ.payload
        else:                 #父节点，一个孩子 六种情况
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.leftChild.parent = node.parent
                    node.patent.leftChild = node.leftChild
                elif node.isRightChild():
                    node.leftChild.parent  = node.parent
                    node.patent.rightChild = node.leftChild
                else:
                    node.replaceNodeData(node.leftChild.key,
                                         node.leftChild.payload,
                                         node.leftChild.leftChild,
                                         node.leftChild.rightChild)
            else:
                if node.isLeftChild():
                    node.rightChild.parent = node.parent
                    node.patent.leftChild  = node.rightChild
                elif node.isRightChild():
                    node.rightChild.parent = node.parent
                    node.patent.rightChild = node.rightChild
                else:
                    node.replaceNodeData(node.rightChild.key,
                                         node.rightChild.payload,
                                         node.rightChild.leftChild,
                                         node.rightChild.rightChild)
    def findSuccessor(self):
        '''找到后继节点，在右子树的最小左子树位置'''
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin() 
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        '''找到最小左子树'''
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        '''删除后继节点'''
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild  = None 
            else:
                self.parent.rightChild = None 
        elif self.hasChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild  = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent      = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild  = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent     = self.parent
        else:
            pass
    #/*************3.删除二叉搜索树节点的相关函数结束****************/# 
########################################################################
#常见的数据结构的Map ADT的时间复杂度
operation   Sorted List     Hash Table      BinarySearchTree      AVLTree
put           O(n)             O(1)              O(n)             O(log2n)
get           O(log2n)         O(1)              O(n)             O(log2n)
in            O(log2n)         O(1)              O(n)             O(log2n)
del           O(n)             O(1)              O(n)             O(log2n)

