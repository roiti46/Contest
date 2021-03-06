def solve(i,j):
    if dp[i][j] != -1: return dp[i][j]
    res = 0
    if j>=2 and i+2<=n:
        res += solve(i+2,j-2)*(i+2)*(i+1)/2
    if i+1<=n:
        res += solve(i+1,j)*(i+1)*j
    if j+2<=n:
        res += solve(i,j+2)*(j+2)*(j+1)/2
    res %= mod
    dp[i][j] = res
    return res


n,m,mod = map(int,raw_input().split())
col = [2]*n
for _ in range(m):
    mtrx = raw_input()
    for i in range(n):
        if mtrx[i] == 1: col[i] -= 1

r1 = r2 = 0        
for i in col:
    if   i == 2: r2 += 1
    elif i == 1: r1 += 1
dp = [[-1]*(n+1) for _ in range(n+1)]
dp[r2][r1] = 1

print solve(0,0)
