#쉬운 최단거리
import sys
#BFS

n,m = map(int,sys.stdin.readline.split())
queue = []
#처음 다 방문 x로 초기화
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        #0 || 1 || 2
        num = list(map(int,input().split()))
        if num[i][j]==2:
            queue.append((i,j))
            #방문 후 true로
            visited = True



