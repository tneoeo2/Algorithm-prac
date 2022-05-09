#%%
from nis import cat
from turtle import Turtle
from uuid import RFC_4122


a = int(input())  #입력은 월하나
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



if a == months[-1] or a in months[0:2]:
    print("winter")
elif a in months[2:5]:
    print("spring")
elif a in months[5:8]:
    print("summer")
else:
    print("fall")
# %%

n = 1 #처음 검사 통과위해 0 아닌 임의값 설정

while n!=0:
    n = int(input())
    if n!=0:
        print(n)
    else:
        break
    
 



# %%
n = int(input())

while n in range(1, 101):
    print(n)
    n = n-1
    
# %%
n = int(input())

while n in range(1, 101):
    n = n-1
    print(n)
    
# %%

c = ord(input())  
t = ord('a')
while t <= c:
    print(chr(t), end=" ")
    t += 1
#%%
n = int(input())
t = 0
while t <= n:
    print(t)
    t += 1

#%%
n = int(input())
for i in range(n+1):
    print(i)
# %%
n = int(input())
s = 0
for i in range(1, n+1):
    if i%2 == 0:  #짝수이면 
        s+= i   #더하기
print(s)
    
#%%

n = ord('a')
while n!= ord('q'):
    n = ord(input())
    print(chr(n))
    
# %%
n = int(input())
t = 0

for i in range(1, n+1):
    t += i
    # print('t', t,'i',  i)
    if t >= n:
        print(i)
        break
# %%

n, m = input().split()
n = int(n)
m = int(m)


for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)
        
#%%

n = int(input(), 16)

for i in range(1, 16):
    print("%X*%X=%X" % (n, i, n*i))

# %%
##? 3 6 9 게임의 왕이 되자
n = int(input())

for i in range(1, n+1):
    if i%10==3 :
        print("X", end=' ')
    elif i%10==6 :
        print("X", end=' ')
    elif i%10==9 :
        print("X", end=' ')
    else:
        print(i, end=" ")


# %%
r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
print(r*g*b)
        

# %%
##? 6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
'''
h: 1초 동안 마이크로 소리 강약을 체크하는 횟수
b: 한 번 체크한 값을 저장할 때 사용하는 비트 수
c: 좌우 소리를 저장할 트랙 개수인 채널 수 (모노: 1, 스테레오: 2)
s: 녹음할 시간(sec)

ex) CD음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장
44100*16*2*1bit 공안 필요,
4410*16*2*1/8/1024/1024 => 약 0.168MB 필요

8 bit(비트)           = 1byte(바이트)       # 8bit=1Byte
1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
1024 KB(210 KB)      = 1MB(메가 바이트)
1024 MB(210 MB)     = 1GB(기가 바이트)
1024 GB(210 GB)      = 1TB(테라 바이트)
'''

###? 저장공간 MB단위로 바꾸어 출력, 
###? 소수점 첫째 자리까지 정확도로 출력 MB는 공백을 두고 출력
h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h*b*c*s/8/1024/1024, 1),'MB')

#%%
##! 그림파일 저장용량 구하기
w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

# print(round(w*h*b/8/1024/1024, 2),'MB') #round사용시 불필요한 0 삭제
#ex) round(0.005, 2) => 0.0
print('%.2f'%float(w*h*b/8/1024/1024),'MB')

#%%
##? [기초-종합] 거기까지! 이제 그만~

n = int(input())

s = 0
c = 1

while s < n:
    s += c
    c += 1
    
print(s)

#%%
##? 3의 배수는 통과
n = int(input())

s = 0

while s < n:   #s==n이면 반복문 탈출
    s += 1
    if s % 3 == 0 :  #3의 배수이면
        continue   #다음 반복문으로 넘어감
    print(s, end=' ')
    

#%%
##? 수 나열하기1
a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)

print(a+ d*(n-1))

#%%
##? 수 나열하기2
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)


print(a*(r**(n-1)))

#%%
##? 수 나열하기3
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n+1):
    # print(f's: {s}, m: {m}, d: {d}')
    if i == n :
        print(a)
    a = (a*m) + d
    
#%%
##? 함께 문제 푸는 날
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = 1

while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
print(d)


#%%
##? 이상한 출석 번호 부르기

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])    #a의 문자 int로 캐스팅후 차례로 반환

d=[]
for i in range(24):
    d.append(0)    #0인 요소를 23개 가진 리스트

for i in range(n): #번호 부를시  해당 카운트 +1
    d[a[i]] += 1
    
for i in range(1, 24):   #카운트값 공백두고 출력
    print(d[i], end=' ')
    
    
#%%
##? 이상한 출석 번호 부르기2
n = int(input())  #부른 횟수
call = input().split()
d = []
for i in call:
    d.append(i)

for i in range(len(d)):
    print(d[len(d)-1-i], end=" ")
    
#%%
##? 이상한 출석 번호 부르기3
n = int(input())
call = input().split()  #문자열리스트
d = []

for i in call:
    d.append(int(i))

d.sort()


print(d[0])

    
# %%
##? 바둑판에 흰 돌 놓기
d = []
for i in range(20):   #(19,19) 리스트 만들기
    d.append([])  #리스트안에 다른 리스트 추가
    for j in range(20):
        d[i].append(0)   #리스트 안에 들어있는 리스트 안에 0추가해넣기
        
n = int(input())    ##흰돌 개수
for i in range(n):      
    x, y = input().split()
    d[int(x)][int(y)] = 1
    
for i in range(1, 20):    #좌표 1~19까지여서 range(1, 20)
    for j in range(1, 20):
        print(d[i][j], end=' ')  #r공백 두고 한 줄 출력
    print()   #줄 바꿈
    
# %%
##?바둑알 십자 뒤집기 
# ##! 정리필요
d = [] #list(map(함수, 리스트)) : 리스트의 요소를 지정함수로 처리

for i in range(20): 
    d.append([])
    for j in range(20): 
        d[i].append(0)

for i in range(19):  #리스트 하나씩 입력
    a = input().split()   
    for j in range(19):
        d[i+1][j+1] = int(a[j])   #d[1][1] 번째부터 입력


n = int(input())

for i in range(n):
    x, y = input().split()
    
    for j in range(1, 20):
        if d[j][int(y)]==0:
            d[j][int(y)]=1
        else:
            d[j][int(y)]=0
            
        if d[int(x)][j]==0:
            d[int(x)][j]=1
        else:
            d[int(x)][j]=0

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
            
# %%
##? 설탕과자 뽑기
'''
세로 : h, 가로 : w, 막대 개수: n, 막대길이: l
막대 방향 (d : 0, 세로 1)
좌표(x, y)

'''
#!!!!!
c = []   #격자
h, w = input().split()

for i in range(int(h)+1):   #격자 생성
    c.append([])
    for j in range(int(w)+1):
        c[i].append(0)
        
n = int(input())   #막대수 생성

for i in range(n):

    l, d, x, y = input().split()

    if int(d) == 0 :   #가로 배치
        for j in range(int(l)):
            c[int(x)][int(y)+j] = 1
    elif int(d) ==1 :   #세로 배치
        for j in range(int(l)):
            c[int(x)+j][int(y)] = 1
        

for i in range(1, int(h)+1):
    for j in range(1, int(w)+1):
        print(c[i][j], end=" ")
    print()
#%%
###?  성실한 개미
##!
n= []
for i in range(10):
    n.append(list(map(int, input().split())))

x, y = 1, 1   #개미집 출발

while True:
    if n[x][y] == 0:   #현위치 9번
        n[x][y] = 9
    elif n[x][y] == 2:  #밥이다
        n[x][y] = 9
        break
        
    if (n[x+1][y] == 1 and n[x][y+1] ==1): 
        break
    
    if n[x][y+1] != 1:
        y += 1    #가로 이동
    elif n[x+1][y] != 1:
        x += 1   #세로 이동
        
        
        
        
for i in range(10):
    for j in range(10):
        print(n[i][j], end=' ')
    print()
    

                




# %%
