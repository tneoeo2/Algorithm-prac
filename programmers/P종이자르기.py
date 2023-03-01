'''
#*종이 자르기

머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.


#*제한사항
0 < M, N < 100
종이를 겹쳐서 자를 수 없습니다.


#*입출력 예
M	N	result
2	2	3
2	5	9
1	1	0

'''

#각 조각이 1*1이 되도록 잘라야함

def solution(M, N):
    answer =0       #자른 횟수
    
    for i in range(M):
        if i > 0 :      #M과N의 길이가 1이 될때까지 자른다
            answer += 1
        for j in range(N):
            if j > 0 :
                answer += 1
                
    return answer

print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))