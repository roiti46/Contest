alpha = "abcdefghijklmnopqrstuvwxyz"
alpha += alpha.upper()
shist = {i:0 for i in alpha}
thist = {i:0 for i in alpha}

s = raw_input()
t = raw_input()
for i in s: shist[i] += 1
for i in t: thist[i] += 1
y = w = 0
for i in alpha:
    y += min(shist[i],thist[i])
    if shist[i] <= thist[i]:
        thist[i] -= shist[i]
        shist[i] = 0
    else:
        shist[i] -= thist[i]
        thist[i] = 0
for i in alpha:
    j = i.upper() if i.islower() else i.lower()
    w += min(shist[i],thist[j])
    if shist[i] <= thist[j]:
        thist[j] -= shist[i]
        shist[i] = 0
    else:
        shist[i] -= thist[j]
        thist[j] = 0    
print y,w
