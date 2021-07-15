stce = input('Enter : ')

s_list = stce.split(' ') #공백 기준 절삭

while '' in s_list: #문자열 양쪽 공백 없어질때까지 반복
    s_list.remove('') #문자열 양쪽 공백 제거

print(len(s_list))
