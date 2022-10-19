 #? 수 정렬하기 3
 
 
 
 
N = int(input())

n_list = []

for i in range(N):
    n_list.append(int(input()))
    
    
n_list.sort()

for n in n_list:
    print(n)
 