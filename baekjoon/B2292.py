'''

a -> b -> c
6 -> 12 -> 18   ==> 6개씩 증가
r = a-1   배수
1 -> 4 -> 13     ###이전 값 +  1번 수 -1 * n번
1 -> 1 + 1*3  -> 4 + 3*3


'''
n = int(input()) 

bnum = 1    #벌집 수
bdepth = 1 #벌집 깊이?

while n > bnum:     #입력한 값 <= 벌짚깊이 == 최소거리
    bnum += 6*bdepth
    # print("bnum",bnum)
    bdepth +=1
    # print("bdepth",bdepth)
print(bdepth)   