'''
#*문제 설명
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

#*제한사항
1 ≤ my_str의 길이 ≤ 100
1 ≤ n ≤ my_str의 길이
my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.

#*입출력 예
my_str	n	result
"abc1Addfggg4556b"	6	["abc1Ad", "dfggg4", "556b"]
"abcdef123"	3	["abc", "def", "123"]

'''

def solution(my_str, n):
    num = len(my_str)//n
    answer = []
    for i in range(num):
        answer.append(my_str[i*n: (i+1)*n])
    # if len(my_str)%n != 0:
    #     answer.append(my_str[num*n:])
    return answer


print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))


#%%

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
'''
0~len(my_str) 까지 n개씩 증가
ex) my_str[0: 0 + 3] , my_str[3: 3 + 3] 
일정한 수로 배열 반환가능

'''
