 #? 통계학

#정수의 절댓값 4,000 넘지않는다.

#1. 산술평균 : 소수점이하 첫째자리에서 반올림 
#2. 중앙값
#3. 최빈값 : 여러 개 있을 시, 최빈값 중 작은 값 출력

import sys
from collections import Counter
import time

def aver(nums: list):  #산술평균 구하는 함수
    
    aver = sum(nums) / len(nums)
    
    return round(aver)

def mid_num(nums: list): #중앙값 구하는 함수
    idx = len(nums)//2   #중앙값을 가지는 인덱스 
    nums.sort(reverse=True)   #오름차순 정렬
    
    return nums[idx]

def freq_num(nums: list): #최빈값 구하는 함수
    """
    dup = list(set(nums))
    dup_cnt = [0] * len(dup)    #중복값 수 저장할 리스트 생성
    dup_dict = {}
    for n in nums:
        for i in range(len(dup)):
            if dup[i] == n:
                dup_cnt[i] += 1
                dup_dict[dup[i]] = dup_cnt[i]
    
    sorted_dup_dict = dict(sorted(dup_dict.items(), reverse=True))  #value기준 내림차순 정렬
    
    values = list(sorted_dup_dict.values())
    keys = list(sorted_dup_dict.keys())
    if values[0] == values[1] :     #최대값이 2개 이상일 경우,
        return keys[1]
    else:
        return keys[0]
    """
    nums.sort()
    cnt_li = Counter(nums).most_common()   # EX)[(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)] 형태로 전환 값: 값_cnt
    if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1] : #최빈값 2개 이상일 경우, 
        return cnt_li[1][0]    #두번째로 작은값 출력
    else:   #최빈값 1개일 경우
        return cnt_li[0][0]    #가장 작은값출력
    
def range_num(nums: list): #최대-최소 구하는 함수
    max_num = max(nums)
    min_num = min(nums)
    
    return max_num - min_num
    
      
N = int(sys.stdin.readline())   #N은 홀수이다.   #input()코드로 받을 시 시간초과

n_list = [0] * N    #배열 미리 만들어두기

for i in range(N):
    n_list[i] = int(sys.stdin.readline())   #input()코드로 받을 시 시간초과


# print(n_list)

print(aver(n_list))
print(mid_num(n_list))
print(freq_num(n_list))
print(range_num(n_list))
    

