 ##? 덩치
 
'''
몸무게 : x, 키 : y  -> (x, y)
  
'''
import sys
input = sys.stdin.readline

N = int(input())   # 전체 사람의 수

info = []
for _ in range(N):
    x, y = map(int, input().split())   #몸무게, 키 입력 받음
    info.append((x, y))
    
for i in info:
    rank = 1
    for j in info:
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end =" ")
    
    