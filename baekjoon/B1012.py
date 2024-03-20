'''
유기농 배추
1.인접한 배추끼리는 벌레 이동가능
-> 인접(상하좌우) 배추 보호 받음 : 같은 행, 열
2. 인접한 배추 묶음 당 벌레 1 투입
'''
import sys
from collections import deque
input = sys.stdin.readline


# def solution(T, info, coords):
#왼 오 위 아
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input()) #테스트케이스의 개수


# m, n, k = 10, 8, 17


# k_li = [(0, 0), (1, 0), (1, 1), (4, 2), (4, 3), (4, 5), (2, 4), (3, 4), (7, 4), (8, 4), (9, 4), (7, 5), (8, 5), (9, 5), (7, 6), (8, 6), (9, 6)]

# print('graph:', graph)
#1인 경우만 bfs 함수 탄다
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1 #방문처리
    while q:
        # print('q: ', q)
        x, y = q.popleft()
        for i in range(4):#이동할 좌표 구하기(상, 하, 좌, 우)
            nx = x + dx[i]  
            ny = y + dy[i]
            
            if nx >= 0 and nx < m and ny >= 0 and ny < n: #밭 범위 초과
                if graph[nx][ny] == 1 and visited[nx][ny] == 0: #인접 배추라면
                    q.append((nx, ny)) #해당 노드로 이동
                    visited[nx][ny] = 1
                    
for i in range(T): 
    m, n, k = map(int, input().split())
    graph = [[0]*50 for _ in range(50)]  #최대 크기 밭으로 고정 생성
    visited = [[0]*n for _ in range(m)]
    cnt = 0
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1         
             
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:  #배추 있는 경우
                bfs(i, j)
                cnt += 1
    print(cnt)    
# t_cord = ["0 2", "1 2", "2 2", "3 2", "4 2", "4 0"]

# solution(1, "5 3 6", t_cord)

# https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94