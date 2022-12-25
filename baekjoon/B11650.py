#좌표 정렬하기
#N :  평면위 점의 개수
# 작은 x -> 큰 x
# x가 같은 경우  작은 y -> 큰 y
import sys
input = sys.stdin.readline

N = int(input())
coord_list = []

for i in range(N):
    a= list(map(int, input().split()))
    coord_list.append(a)

# print(coord_list)
# print(sorted(coord_list))    #리스트째로 정렬이 가능하다니..!! 엄청나다 파이썬!
coord_list = sorted(coord_list)
for i in range(N):
    print(coord_list[i][0], coord_list[i][1])


    

    
