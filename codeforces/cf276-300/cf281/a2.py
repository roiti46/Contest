team1 = raw_input()
team2 = raw_input()
red1,red2,yellow1,yellow2 = [],[],[],[]
for roop in range(int(raw_input())):
    t,ha,m,yr = raw_input().split()
    if ha == "h":
        if m in red1: continue
        if yr == "r" or (yr == "y" and m in yellow1):
            print team1,m,t
            red1.append(m)
        else:
            yellow1.append(m)
    else:
        if m in red2: continue
        if yr == "r" or (yr == "y" and m in yellow2):
            print team2,m,t
            red2.append(m)
        else:
            yellow2.append(m)
