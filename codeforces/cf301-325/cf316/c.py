n, m = map(int, raw_input().split())
s = list(raw_input())

cnt = ans = 0
for si in s:
    if si == ".":
        cnt += 1
    else:
        ans += max(0, cnt - 1)
        cnt = 0
ans += max(0, cnt - 1)

for loop in xrange(m):
    x, c = raw_input().split()
    x = int(x) - 1
    if c == "." and s[x] == "." or c != "." and s[x] != ".":
        pass
    elif c == "." and s[x] != ".":
        cnt = 0
        if x > 0     and s[x - 1] == ".": cnt += 1
        if x < n - 1 and s[x + 1] == ".": cnt += 1
        ans += cnt
    elif c != "." and s[x] == ".":
        cnt = 0
        if x > 0     and s[x - 1] == ".": cnt += 1
        if x < n - 1 and s[x + 1] == ".": cnt += 1
        ans -= cnt
    s[x] = c
    print ans
    
