import sys
#sys.stdin = open("cheatingtree\input.txt") # comment this section to read from keyboard
nodes = []
memo = {}
M = 10**9+7

def dfs(idx, target, nodes):
    if idx*2 + 1 >= len(nodes):
        if nodes[idx] == [0]:
            return [0, M]
        return [M, 0]
    
    memo[idx] = [M,M]
    left = dfs(idx*2 + 1, target, nodes)
    right = dfs(idx*2 + 2, target, nodes)

    g, c = nodes[idx]
    if g == 0:
        for i in range(len(left)):
            for j in range(len(right)):
                l = left[i]
                r = right[j]
                if l != M and r != M:
                    memo[idx][i or j] = min(memo[idx][i or j], l + r)
    else:
        for i in range(len(left)):
            for j in range(len(right)):
                l = left[i]
                r = right[j]
                if l != M and r != M:
                    memo[idx][i and j] = min(memo[idx][i and j], l + r)
    if c == 1:
        if g == 0:
            for i in range(len(left)):
                for j in range(len(right)):
                    l = left[i]
                    r = right[j]
                    if l != M and r != M:
                        memo[idx][i and j] = min(memo[idx][i and j], l + r + 1)
        else:
            for i in range(len(left)):
                for j in range(len(right)):
                    l = left[i]
                    r = right[j]
                    if l != M and r != M:
                        memo[idx][i or j] = min(memo[idx][i or j], l + r + 1)
    return memo[idx]
   
    
def runTests():
    tests = int(input())

    for t in range(tests):
        m, v = map(int, input().split())
        target = v
        nodes = []
        for i in range(m):
            nodes.append(list(map(int, input().split())))
        res = dfs(0, target, nodes)[target]
        if res == M:
            print(f"Case #{t + 1}: IMPOSSIBLE")
        else:
            print(f"Case #{t + 1}: {res}")

runTests()

    