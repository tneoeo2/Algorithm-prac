 ##?소트인사이드
 #수의 각 자리수를 내림차순으로 정렬해보자
 
 
 
N = int(input())

li = list(map(int, str(N)))
# print(li)

li.sort(reverse=True)

for i in li :
    print(i, end='')

    
