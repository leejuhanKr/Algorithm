import sys
input=sys.stdin.readline
t=True
s=True
a,b=0,0
for _ in range(int(input())):
    n=input().rstrip()
    t=True;a=0
    for i in range(len(n)):
        if n[i] == "(":
            a+=1
        elif n[i]==")":
            a-=1
        if a <0:
            t=False
    if a!=0:
        t=False
    print(["NO","YES"][t])