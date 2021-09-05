
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
str = input()
res = 0
for j in range(len(str)) : #str의 길이 만큼 반복
    # print(j)
    for i in dial : #다이얼 리스트 길이만큼 반복
        if str[j] in i :    #str[j]의 문자가 i와 일치할 때
          res+= dial.index(i)+3    #dial의 인덱스 +3
print(res)