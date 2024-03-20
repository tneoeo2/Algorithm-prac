#비밀번호 찾기
'''
- 사이트 주소 구분 : 소문자, 대문자, -, . (중복 없음)
- 비밀번호 : 대문자
'''
n, m = map(int, input().split())

site_map = {}

for _ in range(n):
    name, pw = input().split()
    site_map.setdefault(name, pw)
    
for _ in range(m):
    name = input()
    print(site_map.get(name))