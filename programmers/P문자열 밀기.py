'''

#* 문제 설명 
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다.
이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 
최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.


#* 제한사항
0 < A의 길이 = B의 길이 < 100
A, B는 알파벳 소문자로 이루어져 있습니다.

#* 입출력 예
A	B	result
"hello"	"ohell"	1
"apple"	"elppa"	-1
"atat"	"tata"	1
"abc"	"abc"	0


'''

def solution(A, B):
    answer = 0      #민 횟수
    num = len(A)-1
    if A == B:              #A와 B가 문자일경우 
        return answer
    
    for idx, i in enumerate(A[:num]):
        # print("idx : ", idx)
        result = A[-1]   #수정된 문자
        for _, j in enumerate(A[:num]):
                result += j
                
        # print("result: " + result)
        answer += 1
        if result == B:
            return answer
        elif idx == num-1: #반복문 다돌았는데도 일치X 
            print("반복문 완")
            if result != B:
                return -1
            
        A = result          #
       

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))




#%%?????
solution=lambda a,b:(b*2).find(a)

# def solution(a,b):
#     answer = b*2
#     print(answer)
#     answer = answer.find(a)
#     print("answer: ", answer)


print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))

