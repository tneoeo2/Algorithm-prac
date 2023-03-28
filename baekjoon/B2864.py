'''
*5와 6의 차이
--문제
상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.

상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

--입력
첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)

--출력
첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.

'''
 

A, B = input().split()
result = 0      # 최솟값 : 5로 본다 , 최댓값 : 6으로 본다.

def get_max(nums: list, bf: str, af: str): 
    """
    nums : 입력받은 숫자 (2개)
    bf : 변경 전 문자
    af : 변경 후 문자
    """
    result = 0
    
    for n in nums:
        if bf in n:
            n = n.replace(bf, af)
        result += int(n)
            
    return result


print(get_max([A, B], '6', '5'))
print(get_max([A, B], '5', '6'))
        
# for n in (A, B):
#     if '6' in n:
#         n.replace('6', '5')
#         result += int(n)
        
# print(result, end=' ')
    
# for n in (A, B):
#     if '5' in n:  #최댓값 구하기
#         n.replace('5', '6')
    
# print(result)
    
    
        
        


