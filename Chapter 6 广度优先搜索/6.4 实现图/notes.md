### 实现图
用代码实现算法前，得用代码把图表示出来。图由多个节点构成，每个节点与自己的朋友节点直连。散列表可以很好的表示映射关系，而每个节点有多个朋友节点，就是一对多的关系。可以把散列表的值，用列表存储多个朋友节点。

![](图例6.4.png)

用Python代码表示此图的关系：

```Python
graph={}
graph['you']=['alice', 'bob', 'claire']
graph['bob']=['anuj', 'peggy']
graph['alice']=['peggy']
graph['claire']=['thom', 'jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]
```

Anuj、Peggy、Thom和Jonny都没有邻居，这是因为虽然有指向他们的箭头，但没有从他们出发指向其他人的箭头。这被称为有向图（directed graph），其中的关系是单向的。因此，Anuj是Bob的邻居，但Bob不是Anuj的邻居。无向图（undirected graph）没有箭头，直接相连的节点互为邻居。下图所示的有向图与无向图是等价的：

![](图例.png)

