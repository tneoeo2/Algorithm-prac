 #? 커트라인
 
 #응시자수 : N
 #상을 받는 사람의 수 : k
 #각 학생의 점수 : x
 
N, k = map(int, input().split())

x = list(map(int, input().split()))

x.sort(reverse=True)   #내림차순 정렬

print(x[k-1])




    

 