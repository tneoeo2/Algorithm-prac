 ##? 회의실 배정 (그리디 알고리즘)

import sys

input = sys.stdin.readline

n = int(input())        #회의의 최대개수

sess = []

start, end = map(int, input())  #회의 시작시간, 회의 끝나는 시간

for _ in range(n):
    sess.append([start, end])


sess.sort(key=lambda x: (x[1], x[0])) #회의 끝나는 시간 기준 오름차순-> 시작 시간 기준 오름차순   

time = 0
answer = 0
for s in sess:
    if time <= s[0]:   # 비교할 회의 시작시간이 가장 최근 회의으 끝나는 시간 이후 일 경우
        time = s[1]     # time 회의 끝나는 시간으로 변경
        answer += 1      #회의 개수 +1  
        
print(answer)
    
'''
가장먼저 끝나는 회의 기준으로 비교
'''

