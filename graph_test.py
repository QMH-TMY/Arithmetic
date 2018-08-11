# -*- coding:UTF8 -*-
#!/usr/bin/python
#Shieber on 2018/8/8
#图及其结构

from graph import Graph
from queue import Queue,PriorityQueue

#********************问题1****************************************#
def buildCharGraph(wordFile):
    '''字梯圖'''
    wdLis = {}
    graph = Graph()
    wfile = open(wordFile,'r')

    for line in wfile:
        word = line[:-1] #去掉换行符
        for i in range(len(word)):
            sig = word[:i] + '_' + word[i+1:]
            if sig in wdLis:
                wdLis[sig].append(word)
            else:
                wdLis[sig] = [word]

    for sig in wdLis.keys():
        for word1 in wdLis[sig]:
            for word2 in wdLis[sig]:
                if word1 != word2:
                    graph.addEdge(word1,word2)
    return graph 

#G,d = buildCharGraph("wordfile.txt")
#print(G.getVertices())
#print(G.getEdge())
#print(d.keys())

    #*******解决方案********#
def BFS(G,start):
    '''字梯图解决方案:广度优先搜索,时间复杂度:O(V+E)'''
    start = G.getVertex(start)
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue() #加入队列
    vertQueue.enqueue(start)
    
    while vertQueue.size() > 0:
        currVert = vertQueue.dequeue()
        for nbr in currVert.getConnections():
            if 'white' == nbr.getColor():
                nbr.setColor('grey')
                nbr.setPred(currVert)
                nbr.setDistance(currVert.getDistance()+1)
                vertQueue.enqueue(nbr)
        currVert.setColor('black')

def traverse(G,mark):
    '''打印出任意字回到原始字的路径'''
    node = G.getVertex(mark)
    dist = 0
    while node.getPred():
        print(node.getId(),dist)
        dist += 1 
        node = node.getPred()
    print(node.getId(),dist)


#********************问题2****************************************#
def kinghtGraph(size):
    '''骑士之旅图'''
    ktGraph = Graph()
    for row in xrange(size):
        for col in xrange(size):
            currNode = pos2node(row,col,size) #将坐标转换为点数
            legalPos = getPos(row,col,size)   #得到可去的坐标
            for pos in legalPos:
                avalNode = pos2node(pos[0],pos[1],size) 
                ktGraph.addEdge(currNode,avalNode)
    return ktGraph

def getPos(row,col,size):
    '''得到可去的坐标'''
    newMoves   = []
    stepVector = [
                   (-2,-1),(-1,-2),(2,-1),(1,-2), 
                   (-2, 1),(-1, 2),(2, 1),(1, 2) #对于马来说，可以移动的步伐向量
                 ] 
    for step in stepVector: 
        newRow = row + step[0]
        newCol = col + step[1]
        if legal(newRow,newCol,size):
            newMoves.append((newRow,newCol))

    return newMoves

def legal(row,col,size):
    '''判断是否超界'''
    if 0<= row < size and 0<= col < size:
        return True
    else:
        return False

def pos2node(row,col,size):
    '''将坐标转换为点数'''
    return (row * size) + col

#print "point number:%d"%g.numVertice
#print "Edge  number:%d"%g.edgeNumber
#print "space rate  :%.2f%%"%((g.edgeNumber + 0.0)*100/(i**4))

    #*******解决方案1********#
def DFS1(depth,path,vertex,limit):
    '''深度优先树,时间复杂度:O(k^N),非常高'''
    vertex.setColor('grey')
    path.append(vertex)
    if depth < limit:
        nbrList = list(vertex.getConnections())
        done    = False
        index   = 0
        while index < len(nbrList) and not done:
            if 'white' == nbrList[index].getColor():
                done = DFS1(depth+1,path,nbrList[index],limit)
            index += 1
        if not done:
            path.pop()
            vertex.setColor('white')
    else:
        done = True

    return done


    #*******解决方案2********#
def orderByAvail(vertex):
    '''启发式算法,局部搜索'''
    resList = []
    for vet in vertex.getConnections():
        if 'white' == vet.getColor():
            depth = 0
            for w in vet.getConnections():
                if 'white' == w.getColor():
                    depth += 1
            resList.append((depth,vet))

    resList.sort(key=lambda item:item[0])

    return [minivet[1] for minivet in resList]

def DFS2(depth,path,vertex,limit):
    '''深度优先树,结合启发式算法,时间复杂度:O(2^N),'''
    vertex.setColor('grey')
    path.append(vertex)
    if depth < limit:
        nbrList = orderByAvail(vertex) #从短的到长的,反向来
        done    = False
        index   = 0
        while index < len(nbrList) and not done:
            if 'white' == nbrList[index].getColor():
                done = DFS2(depth+1,path,nbrList[index],limit)
            index += 1
        if not done:
            path.pop()
            vertex.setColor('white')
    else:
        done = True

    return done

'''
G = kinghtGraph(8)
path = []
vertex = G.getVertex(0)
DFS2(0,path,vertex,63)
print len(path)
'''

#########################################################
class DFSGraph(Graph):
    '''通用深度优化森林,时间复杂度:O(V+E)'''
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        '''清空点的颜色，从新开始迭代查找'''
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)

        for aVertex in self:
            if 'white' == aVertex.getColor():
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        '''迭代查找'''
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if 'white' == nextVertex.getColor():
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

#########################################################
   #/*******************************/# 
def SCC(DFSgraph1):
    '''强连通分量算法'''
    DFSgraph1.dfs()                   #计算图的完成时间
    finitime1 = sortFini(DFSgraph1)

    DFSgraph2 = transGraph(DFSgraph1) #转置图
    DFSgraph2.dfs()
    finitime2 = sortFini(DFSgraph2,False)

    positionL = [i for i in range(len(fini1)) if fini1time[i] == finitime2[i]]
    graphList = splitList(Olist,positionL)
    return graphList

def sortFini(graph,rever=True):
    '''联通量算法辅助1:将完成时间列表排序'''
    fini = [(item.fini,item.id) for item in graph.vertexList.values()]
    fini.sort(key=lambda item:item[0],reverse=rever) #从大到小排列完成时间
    return fini
            
def transGraph(graph):
    '''连通量算法辅助2:得到一幅图的转置图'''
    newgraph = DFSgraph()
    for vert in graph.vertexList.keys():
        for nbr in vert.getConnections():
            newgraph.addEdge(nbr,vert,vert.getWeight(nbr))         
    return newgraph 

def splitList(Olist,posList):
    '''拆分列表'''
    graphList = [] #总的列表，存储所有小的连通量
    for i in range(len(posList) + 1):
        graphList.append([])

    j = 0 
    leftList = Olist
    for pos in posList:
        if 0 == pos:
            graphList[j] = leftList[pos]
            leftList = leftList[1:]
            j += 1
        elif len(Olist)-1 == pos :
            graphList[j] = leftList[pos]
            leftList = leftList[:pos]
            j += 1
        
    return graphList
    #未完待续
        

   #/*******************************/# 

def dijkstra(G,start):
    '''最短路径算法,时间复杂度:O((V+E)logV)
       需要整个图，实际运用不现实
       距离矢量路由算法只需要一部分图顶点'''
    start = G.getVertex(start)
    start.setDistance(0)
    PriQueue = PriorityQueue() #加入队列
    PriQueue.buildHeap([(v.getDistance(),v) for v in G])
    
    while not PriQueue.isEmpty():
        currVert = PriQueue.delMin()
        for nbr in currVert.getConnections():
            newDist = currVert.getDistance() + currVert.getWeight(nbr) 
            if newDist < nbr.getDistance():
                nbr.setPred(currVert)
                nbr.setDistance(newDist)
                PriQueue.decreaseKey(nbr,newDist)


   #/*******************************/# 
def prim(G,start):
    '''贪婪算法系列算法,时间复杂度:O((V+E)logV + V)'''
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)

    start = G.getVertex(start)
    start.setDistance(0)
    PriQueue = PriorityQueue() #加入队列
    PriQueue.buildHeap([(v.getDistance(),v) for v in G])
    
    while not PriQueue.isEmpty():
        currVert = PriQueue.delMin()
        for nbr in currVert.getConnections():
            newDist = currVert.getDistance() + currVert.getWeight(nbr) 
            if nbr in PriQueue and newDist < nbr.getDistance():
                nbr.setPred(currVert)
                nbr.setDistance(newDist)
                PriQueue.decreaseKey(nbr,newDist)

def getMinPath(G,endpos):
    '''打印出任意顶点回到起点的最短路径'''
    node = G.getVertex(endpos)
    dist = node.getDistance() 
    while None != node.getPred():
        dist = node.getDistance() 
        print(node.getId(),dist)
        node = node.getPred()
    print(node.getId(),dist)

   #/*******************************/# 
