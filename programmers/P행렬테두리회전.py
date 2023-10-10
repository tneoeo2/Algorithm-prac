def solution(rows:int, columns:int, queries:list=None):
    #배열 만들기
    answer = []
    boxs = []
    for row in range(1, rows+1):
        box = []
        for column in range(1, columns+1):
                num = (row-1)*columns+column
                box.append(num)
        boxs.append(box)
        
    for q in queries:
        q = [x-1 for x in q]  #0부터 시작하는 인덱스에 맞춰 하나씩 빼주기
        tmp = boxs[q[0]][q[1]] #왼쪽 위 값 저장(가장 첫번째요소)
        small = tmp
        
        #left (왼쪽 세로)
        for i in range(q[0]+1, q[2]+1): #첫번쨰 요소 제외 다음요소부터 탐색
            boxs[i-1][q[1]] = boxs[i][q[1]]  #y값은 같으니 이니덱스 1로 고정
            small = min(small, boxs[i][q[1]])
        #bottom 
        for i in range(q[1]+1, q[3]+1):
            boxs[q[2]][i-1] = boxs[q[2]][i]
            small = min(small, boxs[q[2]][i])
        #right 
        for i in range(q[2]-1, q[0]-1, -1):
            boxs[i+1][q[3]] = boxs[i][q[3]]
            small = min(small, boxs[i][q[3]])
        #top
        for i in range(q[3]-1, q[1]-1, -1):
            boxs[q[0]][i+1] = boxs[q[0]][i]
            small = min(small, boxs[q[0]][i])
        boxs[q[0]][q[1]+1] = tmp  #!최초의 값 마지막에 입력
        
        answer.append(small)
            
    return answer        
            
        
    
q =  [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(6, 6, q))