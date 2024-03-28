#최대공약수와 최소공배수

nm = list(map(int, input().split()))

a = max(nm)
b = min(nm)

gcd = 1 #최대공약수
lcm = 0 #최소 공배수

for i in range(1, b+1):
    if a%i == 0 and b%i == 0:
        gcd = i #최대공약수 업데이트

lcm = (a*b) // gcd  #최소공배수 공식

        
print(gcd)
print(lcm)
        


