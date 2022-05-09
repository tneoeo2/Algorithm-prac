
#%%
#1998년생인 내가 태국에서는 2541년생?!
n = int(input())

print(n-543)

#%%
#2439 별찍기
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if n-j < i:
            print("*", end="")
        else:
            print(" ", end="")
    print()