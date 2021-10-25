'''
Dijkstra's algorithm
'''
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra(pnode, pcosts, pgraph, pparents):
    while pnode is not None:
        cost = pcosts[pnode]
        neighbors = pgraph[pnode]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if pcosts[n] > new_cost:
                pcosts[n] = new_cost
                pparents[n] = pnode
        processed.append(pnode)
        pnode = find_lowest_cost_node(pcosts)
    return pcosts, pparents

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
costs, parents = dijkstra(node, costs, graph, parents)

print(parents)
print(costs['fin'])

# 习题A的散列表
graph_a = {}
graph_a['start'] = {}
graph_a['start']['a'] = 5
graph_a['start']['b'] = 2
graph_a['a'] = {}
graph_a['a']['c'] = 4
graph_a['a']['d'] = 2
graph_a['b'] = {}
graph_a['b']['a'] = 8
graph_a['b']['d'] = 7
graph_a['c'] = {}
graph_a['c']['fin'] = 3
graph_a['c']['d'] = 6
graph_a['d'] = {}
graph_a['d']['fin'] = 1
graph_a['fin'] = {}

# 习题A花费的散列表
costs_a = {}
costs_a['a'] = 5
costs_a['b'] = 2
costs_a['c'] = infinity
costs_a['d'] = infinity
costs_a['fin'] = infinity

# 习题A父节点的散列表
parents_a = {}
parents_a['a'] = 'start'
parents_a['b'] = 'start'
parents_a['c'] = None
parents_a['d'] = None
parents_a['fin'] = None

# 记录处理过的节点
processed = []

node = find_lowest_cost_node(costs_a)     #在未处理的节点中找出开销最小的节点
costs_a, parents_a = dijkstra(node, costs_a, graph_a, parents_a)

print(parents_a)
print(costs_a['fin'])

# 习题B的散列表
graph_b = {}
graph_b['start'] = {}
graph_b['start']['a'] = 10
graph_b['a'] = {}
graph_b['a']['c'] = 20
graph_b['b'] = {}
graph_b['b']['a'] = 1
graph_b['c'] = {}
graph_b['c']['fin'] = 30
graph_b['c']['b'] = 1
graph_b['fin'] = {}

# 习题B花费的散列表
costs_b = {}
costs_b['a'] = 10
costs_b['b'] = infinity
costs_b['c'] = infinity
costs_b['fin'] = infinity

# 习题B父节点的散列表
parents_b = {}
parents_b['a'] = 'start'
parents_b['b'] = None
parents_b['c'] = None
parents_b['fin'] = None

# 记录处理过的节点
processed = []

node = find_lowest_cost_node(costs_b)     #在未处理的节点中找出开销最小的节点
costs_b, parents_b = dijkstra(node, costs_b, graph_b, parents_b)

print(parents_b)
print(costs_b['fin'])

# 习题C的散列表
graph_c = {}
graph_c['start'] = {}
graph_c['start']['a'] = 2
graph_c['start']['b'] = 2
graph_c['a'] = {}
graph_c['a']['c'] = 2
graph_c['a']['fin'] = 2
graph_c['b'] = {}
graph_c['b']['a'] = 2
graph_c['c'] = {}
graph_c['c']['fin'] = 2
graph_c['c']['b'] = -1
graph_c['fin'] = {}

# 习题C花费的散列表
costs_c = {}
costs_c['a'] = 2
costs_c['b'] = 2
costs_c['c'] = infinity
costs_c['fin'] = infinity

# 习题C父节点的散列表
parents_c = {}
parents_c['a'] = 'start'
parents_c['b'] = 'start'
parents_c['c'] = None
parents_c['fin'] = None

# 记录处理过的节点
processed = []

node = find_lowest_cost_node(costs_c)     #在未处理的节点中找出开销最小的节点
costs_c, parents_c = dijkstra(node, costs_c, graph_c, parents_c)

print(parents_c)
print(costs_c['fin'])