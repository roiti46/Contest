alpha = "abcdefghijklmnopqrstuvwxyz"
s = raw_input()
flag = False
for i in range(len(s)+1):
    for a in alpha:
        ss = list(s)
        ss.insert(i,a)
        if ss == ss[::-1]:
            print "".join(ss)
            flag = True
            break
    if flag: break
else:
    print "NA"
