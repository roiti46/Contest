mod = 10**9+7
t,k = map(int,raw_input().split())

N = 100111
dp = [0]*N
dp[0] = 1
for i in range(1,N):
    if i >= k:
        dp[i] = (dp[i-1] + dp[i-k])%mod
    else:
        dp[i] = dp[i-1]
ans = [1]*N
for i in range(N):
    ans[i] = (ans[i-1]+dp[i])%mod

for roop in range(t):
    a,b = map(int,raw_input().split())
    res = ans[b]-ans[a-1]
    print res if res >= 0 else res+mod
