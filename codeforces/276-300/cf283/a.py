n,m = map(int,raw_input().split())
A = [raw_input() for _ in range(n)]
chr = [""]*n
for c in range(m):
    for r  in range(n-1):
        if chr[r]+A[r][c] > chr[r+1]+A[r+1][c]:
            break
    else:
        for i in range(n): chr[i] += A[i][c]
print m-len(chr[0])
