import sys
sys.stdin = open("brokensword/brokenswords/sample01.in", "r")
n = int(input())
sm = {}
#tblr
for i in range(n):
    inp = input()
    for j in range(4):
        sm[j] = sm.setdefault(j, 0) + (1 if inp[j] == "0" else 0)

hor = sm[3] + sm[2]
virt = sm[0] + sm[1]
swords = min(hor//2, virt//2)
print(sm)

print(swords, virt-swords*2, hor-swords*2)