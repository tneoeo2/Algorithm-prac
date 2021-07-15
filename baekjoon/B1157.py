word = input('Enter word: ').upper()    #단어 모두 대문자로 변환
word_list = list(set(word)) #단어 set에 담아 중복요소 제거 후, list로 만듬
cnt = []    #빈 list 생성

for i in word_list:
    #list의 해당요소가 등장하는 횟수 count에 담아준다
    count = word.count(i)   #count() : 파이썬 내장함수, 등장횟수 리턴함.
    cnt.append(count) #cnt에 count값 담아줌

if cnt.count(max(cnt)) >= 2:        #가장많이 등장한 문자가 2종류 이상이면
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])

# cnt.index(max(cnt)) #max(cnt)값을 가진 인덱스 번호 반환
