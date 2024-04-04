import sys
sys.stdin = open("cheatingtree\input.txt") # comment this section to read from keyboard
nodes = []
memo = {}
M = 10**9+7

def findLeftAndRightBools(target, left, right):
    left_bool = None
    right_bool = None
    if target == 0:
        if left != M:
            left_bool = 0
        else:
            left_bool = 1
        if right != M:
            right_bool = 0
        else:
            right_bool = 1
    else:
        if left != M:
            left_bool = 1
        else:
            left_bool = 0
        if right != M:
            right_bool = 1
        else:
            right_bool = 0
    return [left_bool, right_bool]

def dfs(idx, target, nodes):
    if idx*2 + 1 >= len(nodes):
        return 0 if nodes[idx][0] == target else M
    
    if idx in memo:
        return memo[idx]
    g, c = nodes[idx]
    left = dfs(idx*2 + 1, target, nodes)
    right = dfs(idx*2 + 2, target, nodes)
    bools = findLeftAndRightBools(target, left, right)
    # here should be the calculation that gives the minimum changes necessary to give either a 1 or a 0
    # for this i would need the value returned from the leaf, and I would need to store this returned value
    #   and the number of times it has come up.

    memo[idx] = M
    if c == 1: #is changeable
        if g == 0:
            if bools[0] and bools[1] == target:
                memo[idx] = min(memo[idx], max(left, right) + 1)
        else:
            if bools[0] or bools[1] == target:
                memo[idx] = min(memo[idx], min(left, right) + 1)

    if g == 0:
        if bools[0] or bools[1] == target:
            memo[idx] = min(memo[idx], min(left, right))
    else:
        if bools[0] and bools[1] == target:
            memo[idx] = min(memo[idx], max(left, right))
    return memo[idx]
    
def runTests():
    tests = int(input())

    for _ in range(tests):
        m, v = map(int, input().split())
        target = v
        nodes = []
        for i in range(m):
            nodes.append(list(map(int, input().split())))
        
        print(nodes)
        res = dfs(0, target, nodes)
        if res == M:
            print('impossible')
        else:
            print(res)

runTests()

    