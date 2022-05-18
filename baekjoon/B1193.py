#분수 찾기

n = int(input())

'''
짝수 라인 : 분자 + 1 , 분모 -1
홀수 라인 : 분자 - 1, 분모 +1
'''

line = 0  #라인 수
max = 0 #최댓값 (최대 몇번째 분수까지 허용가능한지...?)

while n > max :  #최댓값이 n보다 작거나 같을 때까지 반복
    line += 1
    max += line
    
diff = max - n    #최댓값과 입력값의 차(ex n=5, max=6, diff=1)

if line%2 ==0 : # n번쨰 분수가 속하는 라인이 짝수
    top = line -diff   #line : 해당 라인의 최대 분모 or 분자 
    bot = 1 + diff
else:
    top = 1 + diff
    bot = line- diff
    
print(f'{top}/{bot}')
    

    
    
