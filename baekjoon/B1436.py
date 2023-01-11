 ##? 영화감독 숌
import sys

input = sys.stdin.readline

n = int(input())     ##몇번쨰 영화인지

movie = 666   #고정값 

while n :
    if "666" in str(movie) :     ##영화이름에 666이 포함되어 있을 시
        n -= 1                  
    movie += 1              
        
print(movie - 1)

 