import sys


#BFS
#첫 시작을 담아
#

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline.split())
    #그래프에 연결된 사람 추가
    graph[a].append(b)
    graph[b].append(a)
    #graph[1]=[3,4]

#BFS 사용
#