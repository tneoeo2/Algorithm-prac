# ##? 동전 0

'''
준규가 가지고 있는 동전은 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고한다. 
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

'''
#%%
##? 그리디 알고리즘

## N : 동전들의 종류
## K : 만들어야할 값

N, K = map(int,input().split())

#동전 종류 리스트 형태로 입력
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)    #동전 내림차순 정렬
#coins = [50000, 10000, 5000, 1000, 500, 100, 50,10, 5, 1]

#coins리스트 안의 동전 < 만들어야 할 값
answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin    #몫만큼 더하기
        K %= coin #나머지 할당
        if K <= 0: #만약 K가 0이면 반복문 탈출
            break
print(answer)    #사용된 동전의 개수

    



# %%
##? 동전 0 재시도
'''
N : 동전의 종류
K : 동전 가치의 합
print : 필요한 동전 개수의 최솟값


* 그리디 알고리즘 : 선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 해답에 도달하는 방법
* 최적해를 구하는 데 사용되는 근사적인 방법 : 여러 경우 중 하나를 결정해야 할때 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행
! 그리디 알고리즘 적용하기위한 2가지 조건
! 1. 탐욕적 선택 속성(Greedy Choice Property) : 앞의 선택이 이후의 선택에 영향을 주지않는다.
! 2. 최적 부분 구조(Optimal Substructure) : 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성된다.

'''

import sys

input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
answer_li = []
for _ in range(n):
    coin.append(int(input()))    #코인 종류 입력받음 : n개의 코인

coin.sort(reverse=True)   #가치가 높은 코인순으로 정렬

for idx, i in enumerate(coin):
    remain = k
    answer = remain//i    #i동전 사용 개수
    remain = remain%i    #i동전 뺀 나머지값         
    for j in coin[idx:]:
        if remain%i == 0:   #남은 값이 0이면 반복문 탈출
            answer_li.append(answer)
            break
        answer += remain//j
        if remain%j == 0:   #남은 값이 0이면 반복문 탈출
            answer_li.append(answer)
            break
        remain = remain%j    #i동전 뺀 나머지값         
    
print(min(answer_li))
        
        
    
        
    

    

