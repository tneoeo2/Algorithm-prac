 #? 좌표 정렬하기2
## 2차원 평면 위에 N개의 점

import sys

input = sys.stdin.readline

n = int(input())
coord_list = []


for i in range(n):
    x, y = map(int, input().split())   #x, y좌표 리스트 만들기
    coord_list.append([y, x])    #x, y 반대로 집어넣음(후  sorted 위해서)
    
s_coord_list = sorted(coord_list)
# print("coord_list : ", coord_list)
# print("s_coord_list : ", s_coord_list)
    
for i in range(n):  #y, x 순으로 된 배열이니 반대로 출력!
    print(s_coord_list[i][1], s_coord_list[i][0])