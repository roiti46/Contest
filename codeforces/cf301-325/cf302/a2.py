n = int(raw_input())
s = raw_input()
if len(set(list(s))) < n: print "NO"
else:
    cnt = 0
    used = [False]*26
    print "YES"
    c = ""
    for si in s:
        if len(c) == 0 or used[ord(si) - ord(a)] or cnt >= n - 1:
            c += si 
        else:
            print c
            c = si
            cnt += 1
        used[ord(si) - ord(a)] = True
    if len(c) > 0: print c
