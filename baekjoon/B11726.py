#2*n 타일링
'''
(1 ≤ n ≤ 1,000)
https://duckracoon.tistory.com/entry/%EB%B0%B1%EC%A4%80-11726-2xn-%ED%83%80%EC%9D%BC%EB%A7%81-%ED%95%B4%EC%84%A4-python
'''
n = int(input())
dp = [0]*1001
#n=1, n=2 미리 선언
dp[1] = 1
dp[2] = 2
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)
    
