##피보나치 수 2

n = int(input())

dp = []


for i in range(n+1):
    if i == 0:
        dp.append(0)    
    elif i == 1:
        dp.append(1)
    else:
        res = dp[i-2] + dp[i-1]
        dp.append(res)
        
print(dp[-1])