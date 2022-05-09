#2439 별찍기
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if n-j < i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
