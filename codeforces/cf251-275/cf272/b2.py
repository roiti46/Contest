import bisect

n = int(raw_input())
p = map(int,raw_input().split())
m = int(raw_input())
q = map(int,raw_input().split())
a = [0]*(n+1)
for i in range(n):
    a[i+1] = a[i] + p[i]

ans = [0]*m
for i in range(m):
    ans[i] = bisect.bisect_left(a,q[i])
for i in ans:
    print i
