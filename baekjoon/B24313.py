##알고리즘 수업 - 점근적 표기 1
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


##(a1-c)*n0 + a0 <= 0 에서 기울기가 양수일 경우에는 무조건 성립하지 않는다.
#! 따라서 a1<=c 조건 추가
if (a1*n0 + a0) <= c*n0 and a1<=c:
    print(1)
else:
    print(0)
