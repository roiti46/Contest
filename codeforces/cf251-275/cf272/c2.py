class Point():
    def __init__(self,x1 = 0,y1 = 0):
        self.x = x1
        self.y = y1

def dist(a,b):
    return (a.x-b.x)**2+(a.y-b.y)**2

def issquare(a,b,c,d):
    m = Point((a.x+b.x+c.x+d.x)/4,(a.y+b.y+c.y+d.y)/4)
    p = [a,b,c,d]
    if dist(p[0],m) == 0:
        return False
    for i in range(1,4):
        if dist(p[i],m) != dist(p[0],m):
            return False
    for i in range(4):
        for j in range(i+1,4):
            if dist(p[i],p[j]) == 0:
                return False
            smul = (p[i].x-m.x)*(p[j].x-m.x)+(p[i].y-m.y)*(p[j].y-m.y)
            vmul = (p[i].x-m.x)*(p[j].y-m.y)-(p[i].y-m.y)*(p[j].x-m.x)
            if (smul != 0 and vmul != 0):
                return False
    return True

n = int(raw_input())
for roop in range(n):
    p = [[Point() for i in range(4)] for j in range(4)]
    for i in range(4):
        xx,yy,a,b = map(int,raw_input().split())
        xa = xx-a
        yb = yy-b
        for j in range(4):
            p[i][j].x = (xa+a)*4
            p[i][j].y = (yb+b)*4
            xa,yb = -yb,xa
    ans = 12345
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (i+j+k+l < ans and issquare(p[0][i],p[1][j],p[2][k],p[3][l])):
                        ans = i+j+k+l
    print ans if ans != 12345 else -1
