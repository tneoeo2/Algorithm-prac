def solution(N, number):
    dp = [[] for i in range(10)]  #조합으로 나올 수 있는 숫자
   
    for i in range(1, 9): #2~8개의 횟수 안에 가능한지 판별
        dp[i].append(int(str(N)*i)) #NNN 추가
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i-j]: 
                    dp[i].append(n1 + n2)
                    dp[i].append(n1 - n2)
                    dp[i].append(n1 * n2)
                    if n2 != 0: dp[i].append(n1//n2)
            
        if number in dp[i] : return i #N을 i번 사용해서 number 만든다.
        
    return -1 #횟수 8초과일 경우 -1반환

print(solution(5, 12))
