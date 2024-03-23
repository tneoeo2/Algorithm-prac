from collections import deque

#요세푸스 문제 0

n, k = map(int, input().split())
q = deque()
answer = []
for i in range(1, n+1):
    q.append(i)
while q:
    # print('q: ', q)    
    q.rotate(-(k-1))
    answer.append(str(q.popleft()))
    
print('<', ', '.join(answer), '>', sep='')