 #? 수정렬하기
cnt = int(input())

num_list = []

for i in range(cnt):
    n = int(input())
    num_list.append(n)
    
num_list.sort()

for i in range(cnt):
    print(num_list[i])