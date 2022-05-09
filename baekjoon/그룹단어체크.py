###그룹단어 체커
'''
그룹단어 : 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우

입력:
첫번째 입력 : N(N~100) --입력받을 문자열 수 설정
단어는 알파벳 '소문자'로만 구성
중복X, 길이 최대 100, 
'''



N = int(input())  #입력받을 문자열의 수 지정

def group_num_test(num):
    arr=[]
    group_num_len = 0  #그룹단어 수

    for i in range(N):        #N만큼 반복
        arr.append(input())    #문자열 arr에 추가
        
    # print(arr[0][0])
    for i in arr:
        # print(f'-----{i}-----')   #i는 단어리스트 하나씩 반환
        group_num = []   #새단어 그룹단어테스트시 초기화
        for idx, j in enumerate(i):  #j는 i를 문자단위로 끊어서 하나씩 반환
            '''그룹단어 구하기: +1의 요소가 이전요소 같으거나,
            이전에 나온적이없고 중복되지 않는 알파벳일경우 그룹단어로 본다.'''
            if not (j in group_num):  #중복된 원소가 아니면 그룹단어에 넣기
                group_num.append(j)
            elif(j == group_num[-1]):   #중복된 원소일 경우 & 이전단어와일치하면 그룹단어로 체크 
                pass
            else:   #중복된 원소 & 이전단어와 불일치 => 그룹단어X 반복문 탈출
                break
            if idx+1 == len(list(i)):  #반복문 마지막요소까지 무사히 도착 => 그룹단어 O
                group_num_len += 1 
    return group_num_len

        
print(group_num_test(N))