from collections import deque


def dfs(graph, vertex, path, order, visited):
    path.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(graph,neighbor,path,order,visited)
    order.append(path.pop())
def topsort(graph):
    visited =set()
    path= []
    order =[]
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph,vertex,path,order,visited)
    return order[::-1]

def courseschedule(n, prerquists):
    graph=[[] for i in range(n)]
    for pre in prerquists:
        graph[pre[1]].append(pre[0])
    visited = set()
    path = set()
    order=[]
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path,order, visited):
                return False
    return True

def courseschedule(n, prerquists):
    graph=[[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for pre in prerquists:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] +=1
    order=[]
    queue= deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbour in graph[vertex]:
            indegree[neighbour] -=1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return len(order) == n