#스택
import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif cmd[0] == 'size':
            print(len(stack))
        elif cmd[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
    else:
        stack.append(cmd[1])
        