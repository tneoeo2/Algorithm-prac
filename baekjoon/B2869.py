##* 달팽이는 올라가고 싶다.
a, b, v = map(int, input().split())

m = 0 #달팽이 올라간 거리
d = 0 #달팽이가 올라가는데 걸린 일수

#v-b 최종 올라가야하는 거리   (마지막 하루는 미끄러지ㅣ 않는다.)
# a-b 하루동안 올라갈 수 있는 높이
d = (v-b)/(a-b) 

if int(d) == d :
    print(int(d))
else:
    print(int(d+1))   #n.1은 +1일 해야함


'''
while m < v : 
    d+= 1 #날짜 추가
    m += a
    if m >= v : 
        break
    
    m -= b
print("m : ", m, "d: ", d)
'''   ##시간초과

