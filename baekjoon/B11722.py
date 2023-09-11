## 가장 긴 감소하는 부분 수열
n = int(input())  #1<= n <= 1000
n_li = list(map(int, input().split()))

dp = [1 for i in range(n)]
'''
ex) 10, 30, 10, 20, 20, 10
이전 값중 max 값저장?
0: 1
1: 3
2: 1
3: 2
'''

for i in range(n):
    for j in range(i):
        if n_li[j] > n_li[i] :   #이전 요소와 비교하여 가장 클경우
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
        
        
    