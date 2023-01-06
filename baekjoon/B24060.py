 ##? 알고리즘 수업 - 병합 정렬1
'''
병합정렬 : 분할 정복 기법과 재귀 알고리즘을 이용한 정렬 알고리즘 
-> 주어진 배열을 원소가 하나 밖에 남지 않ㅇ르 때까지 계속 둘로 쪼갠 후 에 다시 크기순으로 재배열하면서 원래 크기의 배열로 합침
'''

import sys
input = sys.stdin.readline

def mergeSort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L) + 1)//2    #? [:n] 했을 때 n-1까지의 요소만 포함하니까 +1을 하는 듯?
    ##? 배열 2등분
    left = mergeSort(L[:mid]) 
    right = mergeSort(L[mid:])
    
    L2 =[]
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):   #양쪽 배열 모두 남은 요소가 있을경우
        if left[i] < right[j]:   #왼쪽 - 오른쪽 배열 비교 : 왼쪽이 더 작은경우
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:                   #오른쪽이 더 작은경우
            L2.append(right[j])
            ans.append(right[j])
            j += 1
            
    while i < len(left):     #왼쪽배열에 비교하지않은 값이 남은경우
        L2.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):   #오른쪽 배열에 비교하지않은 값이 남은 경우
        L2.append(right[j])
        ans.append(right[j])
        j += 1  
    
    return L2

n, k = map(int, input().split())      #n : 배열의 크기, k : 저장횟수
a = list(map(int, input().split()))

ans = []
mergeSort(a)

if len(ans) >= k:       
    print(ans[k-1])     
else:                       #정답의 길이가 k보다 작을 경우 -1을 반환
    print(-1)