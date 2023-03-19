'''
N과 M (2)

--문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

--입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

--출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.


'''

import sys

input = sys.stdin.readline

# n, m = map(int, input().split())        #1~n까지의 수, m개의 요소를 갖는 행렬
# result = []

# def dfs():
    
#     if len(result) == m:                #탈출조건
#         print(' '.join(str(el) for el in result))
#         return
    
#     for i in range(1, n+1):
#         if i not in result:
#             if len(result) == 0:
#                 result.append(i)
#                 dfs()
#                 result.pop()
#             elif result[-1] < i :
#                 result.append(i)
#                 dfs()
#                 result.pop()
            
    
# dfs()
            
            
            
#%%
'''
다른 사람 풀이
'''
n, m = map(int, input().split())

lst = []

def dfs(start):
    if len(lst) == m:       #탈출조건
        print(' '.join(map(str, lst)))
        return
    
    for i in range(start, n+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)        #수열은 오름차순
            lst.pop()
dfs(1)      #1부터 시작