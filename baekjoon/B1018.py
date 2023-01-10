 ##? 체스판 다시 칠하기
 
import sys

input = sys.stdin.readline

n, m = map(int,input().split())   # 8<= n, m <= 50 #? 가로, 세로의 길이

board = []
result = []
        
for _ in range(n):
    board.append(input())
    
for i in range(n-7):    ##? 최소 8*8 크기이기 때문에  -7해줌 (8칸 확보를 위해)
    for j in range(m-7): #시작점은 검은색, 흰색 두종류 -> 2개의 변수를 준비(draw1, draw2)
        draw1 = 0
        draw2 = 0
            
        for a in range(i, i+8):  #시작점 : i 부터 8칸 탐색
            for b in range(j, j+8): 
                if (a+b) % 2 == 0:   #번갈아가며 색칠하기 위해 %2의 값에 따라 분기 나눔
                    if board[a][b] != 'B':       ##? draw1은 BWBW순이 아니면 +1
                        draw1 +=1
                    if board[a][b] != 'W':   ##? draw2는 WBWB순이 아니면 +!
                        draw2 +=1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1 
                    if board[a][b] != 'B':
                        draw2 += 1
                        
        result.append(draw1)  #두결과 모두 result배열에 추가하고 수정횟수가 적은 배열을 결과로 출력한다.
        result.append(draw2)
        
print(min(result))
                
                
            
        
        