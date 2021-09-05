#input 여러개, 입력받은 값을 공백기준 분리
num1, num2 = input().split()    #split : ()안의 구분자를 기준으로 문자열 분할하여 리스트로 반환
num1 = int(num1[::-1])   #역순으로 저장(첫인덱스부터 역순으로 1칸씩이동)
num2 = int(num2[::-1])

if num1 > num2 : 
    print(num1)
else:
    print(num2)