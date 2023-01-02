 ##? 나이순 정렬
'''
 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들의 나이가 증가하는 순으로, 
 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오
'''

import sys

input = sys.stdin.readline

n = int(input())   #가입한 회원의 수

members = [0 for i in range(n)]

for i in range(n):
    a, b = input().split()
    a = int(a)    #나이 int로 캐스팅
    members[i] = [a, b]
    
members.sort(key=lambda x: x[0])    #[0]번째 인덱스 기준으로 정렬
# print("members : ", members)
for age, name in members:
    print(age, name)