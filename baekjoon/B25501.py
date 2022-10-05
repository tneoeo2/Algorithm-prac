#재귀의 귀재


def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: 
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt)

# print('ABBA:', isPalindrome('AAA'))
# print('ABC:', isPalindrome('ABC'))
# a, b = isPalindrome('ABBA')
# print(a, b)


s_list= []
num = int(input())

for i in range(num):
    s_list.append(str(input()))

# print(s_list)
for s in s_list:    
    a, b = isPalindrome(s)
    print(a, b)
=======
#재귀의 귀재


def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: 
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt)

# print('ABBA:', isPalindrome('AAA'))
# print('ABC:', isPalindrome('ABC'))
# a, b = isPalindrome('ABBA')
# print(a, b)


s_list= []
num = int(input())

for i in range(num):
    s_list.append(str(input()))

# print(s_list)
for s in s_list:    
    a, b = isPalindrome(s)
    print(a, b)
