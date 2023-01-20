 ##? 주유소 (그리디 알고리즘)
'''
 1km == 1l
 1도시 : 1주유소  - 주유소당 리터당 가격 다름
 기름통 무제한
 
 입력 : 도시의 개수, 도로길이, 주유소 기름값(기름값/리터)
 출력 : 최소 비용
 
'''
 
import sys

input = sys.stdin.readline

city = int(input())     #도시개수
road_len = list(map(int,input().split()))     #도로길이
oil_cost = list(map(int,input().split()))     #1l당 기름값


'''
만약 다음 도시 기름값이 이전도시 기름값보다 비싸면 
다음도시 거리만큼

'''
answer = 0
m = oil_cost[0]     #첫도시 주유비용 고정(필수)
for i in range(city-1): #마지막 도시 빼고 반복문
    if oil_cost[i] < m:  #현기름값 < 다음기름값 -> m: 구매할 기름값 교체 
        m = oil_cost[i]
    answer += m* road_len[i]            #도로길이 * 기름값
        
print(answer)   
    
            
        
 