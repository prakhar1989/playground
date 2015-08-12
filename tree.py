from collections import deque

graph = {
    "a": ["c", "b"],
    "b": ["c"],
    "c": ["d"],
    "d": ["b", "f"],
    "e": ["d", "f"],
    "f": ["e"]
}

def bfs(g, s):
    explored, queue = set([s]), deque([s])
    while len(queue):
        v = queue.popleft()
        print v,
        for n in g[v]:
            if n not in explored:
                explored.add(n)
                queue.append(n)

def dfs(g, s, explored):
    if s in explored:
        return False
    print s,
    explored.add(s)
    for n in g[s]:
        if n not in explored:
            dfs(g, n, explored)

def topo(g):
    explored, order = set([]), deque()
    def dfs(s):
        if s in explored:
            return False
        explored.add(s)
        for n in g[s]:
            if n not in explored:
                dfs(n)
        order.appendleft(s)
    for n in g:
        if n not in explored:
            dfs(n)
    return order

"""
for i in range(4):
    print "For BFS {i}:".format(i=i), bfs(graph, i)
    print "For DFS {i}:".format(i=i), dfs(graph, i, set([]))
"""
bfs(graph, "a")
print
dfs(graph, "a", set())
print
topo(graph)
