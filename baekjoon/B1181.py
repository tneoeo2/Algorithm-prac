 #? 단어정렬
"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오
    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전 순으로
    
    
N = input     (1 <= N <= 20,000)
* 문자열의 길이는 50을 넘지 않는다.
**같은 단어가 여러번 입력된 경우에는 한 번씩만 출력한다.

"""
import sys
input = sys.stdin.readline

n = int(input())  #입력받을 문자열의 수

word_list = [0 for i in range(n)]    #문자열수만큼의 요소를 가진 리스트 만들기

for i in range(n):
    word_list[i] = input().strip()

word_list = list(set(word_list))   #? 중복요소 제거

word_list.sort()   #문자열 기준 정렬(알파벳순 정렬)
word_list.sort(key = len)  #문자열 길이 기준 정렬

for i in word_list : 
    print(i)    