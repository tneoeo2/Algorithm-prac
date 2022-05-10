##손익 분기점
'''
A: 고정비용
B: 가변비용
C: 상품가격

손익 분기점 : 총수입 > A + B 

생산 가격 : A + (B*n)

input : A B C
output : 손익분기점

'''


A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

'''
C *n = A + B*n   # 손익분기점
 C > B면  판매량 늘면 손익분기점 넘길 수 있다.
 
 # C = A/n + B     n의 값 구하기
# A/n = C-B
# 1/n = (C-B)/A
'''

if C <= B:   
    print(-1)
else:
    n = int(A / (C-B)) + 1    #손익분기점 == 판매량 대비하여 +1 
    print(n)
