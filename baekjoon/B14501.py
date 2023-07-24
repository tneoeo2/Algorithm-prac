import sys; 

input = sys.stdin.readline
# https://songsunbi.tistory.com/80 --참고
def consult():
    for day in range(N-1, -1, -1):
        t = Work[day][0]  # 상담 소요일
        # 해당 일에 근무하는 경우
        if day + t <= N:
            p = Work[day][1]  # 상담 수입
            # 최대이익 선택
            '''
            dp[day + 1] : 하루 건너뛴 수익
            dp[day + t] + p : 오늘 수익 + 이전까지 최대 수익
            dp[day] : 가장 높은 수익이 나오는 경우
            '''
            dp[day] = max(dp[day + 1], dp[day + t] + p)  

        # 해당 일에 근무하지 않는 경우
        else:
            dp[day] = dp[day + 1]
            

if __name__ == "__main__":
    N = int(input())
    Work = [list(map(int, input().split())) for _ in range(N)]
    dp = [0]*(N+1) # 최대수입 저장용 DP 테이블
    consult()
    print(dp[0])