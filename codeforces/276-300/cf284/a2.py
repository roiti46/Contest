n,x = map(int,raw_input().split())
ans = 0
cur = 1
for loop in xrange(n):
    l,r = map(int,raw_input().split())
    ans += (l-cur)%x + (r-l+1)
    cur = r+1
print ans
