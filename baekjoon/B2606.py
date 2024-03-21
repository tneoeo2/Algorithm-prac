#바이러스- 그래프 탐색
import sys


input = sys.stdin.readline

n = int(input()) #노드의 수(컴퓨터 수)
m = int(input()) #간선 수

graph = {i:[] for i in range(1, n+1)}
visited = [0]*(n+1)

for i in range(1, m+1):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

print(f'graph: {graph}')
print(f'visited: {visited}')
def dfs(v):
    '''
     v: 시작 노드
    '''
    cnt = 0  #바이러스 걸리게 되는 컴퓨터 수
    stack = []
    
    stack.append(v)
    while stack:
        node = stack.pop()
        if visited[node] == 0: #미방문 노드
            visited[node] = 1
            stack.extend(graph[node])
            print(f'stack:{stack}, node:{node}')
            cnt += 1
    print(cnt-1)

dfs(1)
    
    