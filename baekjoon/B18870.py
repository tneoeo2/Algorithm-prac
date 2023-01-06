 ##? 좌표 압축  
import sys

input = sys.stdin.readline

n = int(input())   #입력받을 좌표의 개수
arr = list(map(int, input().split()))  #int로 형변환후 list로 만들기

arr2 = sorted(list(set(arr)))       #중복제거후 정렬
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr : 
    print(dic[i], end = ' ')
    