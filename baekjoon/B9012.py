#괄호

import sys

input = sys.stdin.readline

def vps(T):
    res = 0
    for i in T:
        if i == '(':
            res += 1
        elif i == ')':
            res -= 1
            if res < 0:
                return 'NO'
    
    if res == 0: 
        return 'YES'
    else: 
        return 'NO'
    


cnt = int(input())

for _ in range(cnt):
    print(vps(input()))



    
    
    
    
    
    