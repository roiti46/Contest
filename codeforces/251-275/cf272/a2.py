ref = "qwertyuiopasdfghjkl;zxcvbnm,./"
c = raw_input()
inp = raw_input()
val = -1 if c == "L" else 1
ans = ""
for i in inp:
    ans += ref[ref.index(i)-val]
    
print ans
