#이항 계수1
'''
이항 계수 : 주어진 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 개수
n개의 서로 다른 것들 중에서 k개를 선택하는 것의 조합의 경우의 수를 구한다.
nCk -> factorial(n)//(factorial(k)*factorial(n-k))
'''


import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#조합 공식 nCk = c!/(n-k)!k!
print(factorial(n)//(factorial(n-k) * factorial(k)))