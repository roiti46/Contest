n, m = map(int, raw_input().split())
a = [map(int, raw_input().split()) for i in xrange(m)]

win = [0] * n
for i in xrange(m):
    mx = max(a[i])
    win[a[i].index(mx)] += 1

mx = max(win)
print win.index(mx) + 1
