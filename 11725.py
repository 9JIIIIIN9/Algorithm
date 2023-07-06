def dfs(graph,v,visited):
    visited[v]=True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N=int(input())

tree=[[]for _ in range(N+1)]
parent=[None for _ in range(N+1)]





visited=[False]*9

dfs(graph,1,visited)
