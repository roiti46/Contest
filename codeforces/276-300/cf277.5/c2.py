m,s = map(int,raw_input().split())
ss = s
large,small = [],[1]+[0]*(m-1)
while len(large) < m:
    if ss > 9:
        large.append(9)
        ss -= 9
    else:
        large.append(ss)
        ss = 0
i = m-1        
while i > -1:
    if sum(small) == s: break
    if small[i] == 9: i -= 1
    else: small[i] += 1
if m == 1 and s == 0: print 0,0
elif s < 1 or s > 9*m: print -1,-1
else: print "".join(map(str,small)),"".join(map(str,large))
