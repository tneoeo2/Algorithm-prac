 ##? 행렬 덧셈
 
 # input : 행렬의 크기 (N*M)
 # input2 : A의 행렬 원소 M개
 # input3 : B의 행렬 원소 M개
 
 # ouput : 행렬 A와 B의 합
#* 각 원소 0 < n <= 100
A, B = [], []
N, M = map(int,(input().split()))

'''
##! 처음 풀이
A = [[0]*N]*M
B = [[0]*N]*M
--> 파이썬에서 2차원 리스트 만들 경우 위와 같이 만들경우
ex) [[0,0],[0,0]] --> [0]*N : 깊은 복사 [[0]*N] : 얕은복사 #! 해당리스트 변경시 얕은복사를 통해 생성된 다른 요소가 함께 바뀌므로 사용해선 안된다.

대체 : [[0]*N]*M  -> [[0]*N for _ in range(M)]
'''


for i in range(N) :
    tmp = list(map(int, input().split()))     #배열로 한행씩 받기
    # A[i] = tmp
    A.append(tmp)
        
for i in range(N) :
    tmp = list(map(int, input().split()))     #배열로 한행씩 받기
    # B[i] = tmp
    B.append(tmp)
# print(type(A))
# print("A : ", A)
# print("B : ", B)

for i in range(N) :
    for j in range(M) :
        print(A[i][j] + B[i][j], end=" ")
    print()
