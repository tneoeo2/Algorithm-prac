###? DFS와 BFS
'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
###? True/ False
from collections import deque    #시간복잡도 : queue > deque

N, M, V = map(int, input().split())             

###!! N+1 할것 : 리스트의 인덱스는 0부터 시작하기 때문에 편의상 인덱스 0 버리고 1부터 사용하기 위해서
graph = [[False] * (N+1) for _ in range(N+1)]           ### 그래프를 인접행렬 형식으로 표현
for _ in range(M):
    a, b  = map(int, input().split())
    # 간선의 방향이 양방향 a-> b b-> a 둘다 생각해야한다.
    graph[a][b] = True                  #True 
    graph[b][a] = True
    
visited1 = [False] * (N+1) #dfs의 방문기록
visited2 = [False] * (N+1) #bfs의 방문기록


def bfs(V):
    q = deque([V]) 
    visited2[V] = True  #해당 값 방문처리
    while q : #q가 빌때까지 반복
        V = q.popleft() # 큐의 첫번째 값부터 꺼낸다.
        print(V, end= " ")
        for i in range(1, N + 1): #1부터 N까지 반복
            if not visited2[i] and graph[V][i] : #i값 방문하지 않았고 V와 연결되어 있다면
                q.append(i) #i값 추가
                visited2[i] = True #i값 방문처리
def dfs(V):
    visited1[V] = True  # 해당 V값 방문처리
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited1[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)


dfs(V)
print()
bfs(V)                
                
                


