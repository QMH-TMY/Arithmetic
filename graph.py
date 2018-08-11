# -*- coding:UTF8 -*-
#!/usr/bin/python
#Shieber on 2018/8/8
#图及其结构
###################################################################
#图的一种实现:邻接矩阵
'''
graphＬ = 
[
 ['  ','V0','V1','V2','V3','V4','V5'],
 ['V0',''  ,'5' ,''  ,''  ,''  ,'2' ],
 ['V1',''  ,''  ,'4' ,''  ,''  ,''  ],
 ['V2',''  ,''  ,''  ,'9' ,''  ,''  ],
 ['V3',''  ,''  ,''  ,''  ,'7' ,'3' ],
 ['V4','1' ,''  ,''  ,''  ,''  ,''  ],
 ['V5',''  ,''  ,'1' ,''  ,'8' ,''  ],
]

#图的另一种实现:邻接表,用字典
graphD =
{
  'V0':{'V1':5,'V5':2},
  'V1':{'V2':4}       ,
  'V2':{'V3':9}       ,
  'V3':{'V4':7,'V5':3},
  'V4':{'V0':1}       ,
  'V5':{'V2':1,'V4':8},
}

'''
###################################################################
import sys
class Graph:
    '''图结构'''
    def __init__(self):
        self.vertexList = {}
        self.numVertice = 0
        self.edgeNumber = 0

        #{'New York':{'Beijing' :15432,'Shanghai':15120},
        # 'Sant Sco':{'New York':1276, 'Beijing' :14321},
        # 'Beijing' :{'New York':15432,'Sant Sco':14321},
        #}
        # vertexList的大致结构样式,内部字典为类Vertex的实例

    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self,nv):
        return nv in self.vertexList

    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        self.numVertice += 1 
        return newVertex

    def addEdge(self,frm,to,weight=0):
        if frm not in self.vertexList:
            nv = self.addVertex(frm)
        if to not in self.vertexList:
            nv = self.addVertex(to)
        self.vertexList[frm].addNeighbor(self.vertexList[to],weight)
        self.edgeNumber += 1

    def getVertex(self,vert):
        if vert in self.vertexList:
            return self.vertexList[vert]
        else:
            return None

    def getVertices(self):
        return list(self.vertexList.keys())

class Vertex:
    '''頂點的鏈接點數據'''
    def __init__(self,key):
        self.id    = key         #顶点的名称
        self.connectedTo = {}    #该顶点所有的连接点的信息
        self.color = 'white'     #设置为白色，表示未被探索
        self.dist  = sys.maxsize #设置和起点的距离,数极大
        self.pred  = None        #设置顶点的前导点
        self.disc  = 0           #设置顶点被发现时间
        self.fini  = 0           #设置顶点搜索返回完成时间

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def setDistance(self,dist):
        self.dist = dist

    def setPred(self,pred):
        self.pred = pred
        
    def setColor(self,color):
        self.color = color

    def setDiscovery(self,dtime):
        self.disc  = dtime 
    
    def setFinish(self,ftime):
        self.fini  = ftime 

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        '''每条边的权重'''
        return self.connectedTo[nbr]
        
    def getDistance(self):
        return self.dist

    def getPred(self):
        return self.pred
        
    def getColor(self):
        return self.color
    
#G = Graph()
#a = ['a','b','c','d','e']
#for i in a:
#    G.addVertex(i)
#print(G.vertexList)
#print(G.getVertices())
###################################################################
