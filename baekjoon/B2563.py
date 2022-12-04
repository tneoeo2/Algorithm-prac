 #?색종이
 
##* 가로, 세로 = 100
##* 가로, 세로 = 10


N = int(input())    #색종이의 수
arr = [[0 for _ in range(101)] for _ in range(101)]    #100*100 행렬 미리 만들기 각 행렬의 요소가 가지는 기본값 0으로 설정

for _ in range(N):
    a, b = map(int, input().split())    #검은영역 색종이 수만큼 입력 반복
    for i in range(a, a+10):         #색종이 크기 :10 만큼 이니까 +10까지 반복문 돌기
        for j in range(b, b+10):
            arr[i][j] = 1                   #해당 영역의 값 1로 변경(영역의 넓이의 값과 같다)
            
count = 0

for row in arr:
    #행안에 1의 개수 count에 더함
    count += row.count(1)     #.count() : ()안의 숫자 혹은 문자의 갯수반환
print(count)



    