n,k = map(int,raw_input().split())
f = sorted(map(int,raw_input().split()))[::-1]
ans = 0
while f:
    ans += (max(f[:k])-1)*2
    f[:k] = []
print ans
