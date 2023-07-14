import sys

input = sys.stdin.readline

n = int(input())
nums = []
non_group = 0
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]: #다음 글자와 같은지 비교
            continue
        elif word[j] in word[j+1:]: #다음 글자와 같지 않지만 같은 문자 존재하는 경우
            non_group += 1   #그룹단어 아님 : answer += 1 
            break

print(n-non_group)
            

    
    
    

                
                
    