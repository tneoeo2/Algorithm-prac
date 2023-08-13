##스택 2
import sys
input = sys.stdin.readline
n = int(input())
stack = []

#스택 만들기
for _ in range(n):
    x = list(map(int,input().split()))
    if x[0] == 1:#스택 추가
        stack.append(x[1]) 
    elif x[0] == 2 : 
        #스택 존재시 2번째 값 출력
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif x[0] == 3 :
        print(len(stack))
    elif x[0] == 4 :
        if len(stack) == 0:
            print(1)
        else: 
            print(0)
    elif x[0] == 5 :
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
        