 ##? 최댓값
 
import sys
N = sys.stdin.readline

board = []

for _ in range(9):
    board.append(list(map(int, input().split())))    #9*9의 행렬을 만든다.
    
X = 0       #행
Y = 0       #열
MAX = -1   #최댓값 시작은 -1

for i in range(9):
    for j in range(9):
        if board[i][j] > MAX : #[0][0] ~ [0][n] 까지 값 탐색  기존 최댓값보다 값이 크면 조건문 실행
            MAX = board[i][j]    #최댓값 대체
            X = i+1 
            Y = j+1     #행렬의 인덱스는 리스트 인덱스 의 +1값과 같다(1행부터 시작함)
            
print(MAX)
print(X, Y)

