##? 동전 0

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
