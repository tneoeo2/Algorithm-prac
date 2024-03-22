import sys


sys.setrecursionlimit(10**7)
input = sys.stdin.readline

#연결 요소의 개수
n, m = map(int, input().split())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(f'graph: {graph}')

visited = [0]*(n+1) #방문기록

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0: #방문한 적 없음
            dfs(i)
            
cnt = 0

for i in range(1, n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)
            
            