#수정렬하기 2

##? N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

num = int(input())
n_list = []

for i in range(num):    
    n = int(input())
    n_list.append(n)
    

n_list = sorted(n_list)
    
for i in n_list:
    print(i)