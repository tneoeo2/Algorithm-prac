## 계단 오르기
'''
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
'''

n = int(input())  #계단의 개수
scores = [int(input()) for _ in range(n)]
dp = [0]*(n)  #계단 수별 최댓값을 담는다.

#점화식
# dp[i-3] + scores[i-1] + scores[i] : 두계단 + 이번계단 (한계단 전진)
# dp[i-2] + scores[i] : 두계단 전진

if len(scores) <= 2: #계단이 2개로 끝 
    print(sum(scores))
else:
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])
    print(dp[-1])  #맨마지막 값출력


    

    



