n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
a = sorted(zip(a,range(1,n+1)))
cnt = 0
ans = []
for i in range(n):
    if k >= a[i][0]:
        k -= a[i][0]
        cnt += 1
        ans.append(a[i][1])
print cnt
print " ".join(map(str,sorted(ans)))
