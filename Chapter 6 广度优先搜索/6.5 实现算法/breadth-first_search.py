'''
breadth-first search,BFS
'''

from collections import deque

def person_is_seller(name):
    return name[-1]=='m'

def bfs():
    search_queue = deque()              #创建一个队列
    search_queue += graph['you']        #将你的邻居都加入到这个搜索队列中,这是一个数组。
    searched = []                       #存储已经检查过的人
    while search_queue:                 #只要队列不为空
        person = search_queue.popleft() #取出其中第一个人
        if person in searched:          
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]#不是芒果销售商，则将他的朋友加入队列
            searched.append(person)     #记录已经检查过的人
    return False

graph={}
graph['you']=['alice', 'bob', 'claire']
graph['bob']=['anuj', 'peggy']
graph['alice']=['peggy']
graph['claire']=['thom', 'jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]

bfs()