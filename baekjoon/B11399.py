 #? ATM  (그리디 알고리즘)
 
import sys
input = sys.stdin.readline

n = int(input()) #사람수

time = list(map(int, input().split()))   #돈 인출하는데 걸리는 시간

#시간 최소로 걸리는 경우 구하기
#걸리는 시간 작은 순으로 배치
time.sort()     #오름차순 정렬

answer = 0
for i in range(n):
    for j in time[:i+1]:
        answer += j
print(answer)
        
    
    
