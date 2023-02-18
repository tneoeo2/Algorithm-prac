'''
연속된 세 개의 정수를 더해 12가되는 경우는 3, 4, 5입니다. 두 정수 num과 
total이 주어집니다. 연속된 수 num 개를 더한 값이 total이 될 때, 
정수 배열을 오름차순으로 담아 return 하도록 solution함수를 완성해 보세요.


제한사항
1 ≤ num ≤ 100
0 ≤ total ≤ 1000
num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.


입출력 예
num	total	result
3	12	[3, 4, 5]
5	15	[1, 2, 3, 4, 5]
4	14	[2, 3, 4, 5]
5	5	[-1, 0, 1, 2, 3]
6	15	[0, 1, 2, 3, 4, 5]

'''

def solution(num, total):
    answer = []     #answer는 1씩 증가하는 등차수열이다.
    
    a = total//num
    if total%num == 0:         #이경우, a는 중간 값이다
        start = a-((num-1)//2)  #answer[0] 값
        for i in range(num):
            answer.append(start+i)
    else:               #a는 중간-1값이다
        start = a-(num//2 -1)
        for i in range(num):
            answer.append(start+i)
        
        

    return answer 



print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))