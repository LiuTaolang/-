'''
Dijkstra's algorithm
'''

# 图的散列表
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# 花费的散列表
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 记录处理过的节点
processed = []

node = find_lowest_cost_node(costs)     #在未处理的节点中找出开销最小的节点
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if cost[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)