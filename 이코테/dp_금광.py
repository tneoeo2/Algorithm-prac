'''
n*m 크기의 금광, 각 칸은 특정한 크기의 금이 들어있다
채굴자는 첫번째 열부터 출바라여 금을 캐기 시작한다.

처음은 어디서든 출발 가능
이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽 , 오른쪽 아래 3가지 중 하나의 위치로 이동 가능
return 채굴자가 얻을 수 있는 최대의 금 크기

'''
#input1 : 테스트 케이스 개수 T
#input2 : n, m 공백구분입력
#input3 : n*m 위치에 매장된 금의 개수가 공백으로 구분되어 입력

##? array[i][j] : i행 j열에 존재하는 금의 양
##? dp[i][j] : i행 j열까지의 최적해(얻을 수 있는 금의 최댓값)
##! 점화식 : dp[i][j] + max(dp[i-1][j-1]], dp[i][j-1], dp[i+1][i-1]) -> 왼쪽위, 왼쪽, 왼쪽아래


T = 2
nm1 = [[3, 4], [4, 4]]
golds = [[1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7], [1, 3, 1, 5, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]]

# def gold_mine(test_cnt:int = T, size:list = nm1, golds:list = golds):
'''
test_cnt : 테스트 케이스의 수
size : n*m (넓이 설정)
golds : 각 영역별 매장된 금의 양(n*m개의 수)
'''
for tc in range(int(input())): 
    #금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    #다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = []
    index = 0
for i in range(n):
    dp.append(array[index:index + m])  #금광의 금 매장량 dp에 추가
    index += m
#다이나믹 프로그래밍 진행
for j in range(1, m):  #1번 인덱스부터 시작 / 맨첫 인덱스 빼고 진행
    for i in range(n): 
        #*왼쪽 위에서 오는 경우
        if i == 0 : left_up = 0  #i가 0인경우 첫번째 행이라 왼쪽 위에서 오는게 불가능하니 0으로 처리
        else: left_up = dp[i-1][j-1]
        #*왼쪽 아래에서 오는 경우
        if i== n-1 : left_down = 0 #i가 n-1인 경우, 맨 마지막행 -> 왼쪽아래에서 오는게 불가능 하니 0으로 처리
        else: left_down = dp[i+1][j-1]
        #*왼쪽에서 오는 경우(1에서 시작하여 왼쪽이 없는 경우는 존재하지 않는다.)
        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        
result = 0
for i in range(n):
    result = max(result, dp[i][m-1])#행별 마지막열 비교하며 최대값 구하기
print(result)
        
        
        
        


