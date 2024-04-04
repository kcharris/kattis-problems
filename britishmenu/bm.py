import sys
sys.stdin = open("britishmenu/britishmenu/1.in", "r")

n, m = map(int, input.split())
g = {}

for i in range(m):
    a, b = map(int, input.split())
    g[a].setdefault(a, set()) | b

