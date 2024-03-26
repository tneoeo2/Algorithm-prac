import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
q = deque([])

for _ in range(n):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'pop_front':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif cmd[0] == 'pop_back':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
        elif cmd[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:
                tmp = q.popleft()
                print(tmp)
                q.appendleft(tmp)
        elif cmd[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                tmp = q.pop()
                print(tmp)
                q.append(tmp)
        elif cmd[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'size':
            print(len(q))
            
    else:
        if cmd[0] == 'push_back':
            q.append(cmd[1])
        else:
            q.appendleft(cmd[1])
            