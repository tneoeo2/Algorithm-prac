"""
등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를  
return 하도록 solution 함수를 완성해보세요    

##* 입출력 예
common      result
[1,2,3,4]     5
[2, 4, 8]      16
"""

def solution(common:list):
    #등차수열일 경우
    flg = True              #등차수열 : True, 등비수열 : False
    
    tmp = common[1]-common[0]
    for idx, n in enumerate(common[:len(common)-1]):
        if tmp == common[idx+1]-n:
            flg = True
        else:
            flg =False
    
    if flg == True:     ##등차수열 인경우
        answer = common[-1] + tmp
    elif flg == False:        #등비수열 인경우
        answer = common[-1]*common[1]//common[0]
        
    
    return answer

ex1 = [1, 2, 3, 4]
ex2 = [2, 4, 8]
ex3 = [5, 15, 45, 135]
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))

#%%
'''
'''
def solution(common):
    answer = 0
    a,b,c = common[:3]          #3개만 있음 되니까 뒤에 날림
    if (b-a) == (c-b):          #*등차수열 
        return common[-1] + (b-a)
    else:                       #*등비수열
        return common[-1] * (b//a) 
    
    return answer

ex1 = [1, 2, 3, 4]
ex2 = [2, 4, 8]
ex3 = [5, 15, 45, 135]
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))

# %%
