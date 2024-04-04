# import sys
# sys.stdin = open("frogger/1dfroggerhard/sample1.in", "r")

# travel down lines that have not been gone down yet, find out if it leads to a cycle or an end
# then do a dfs with a building set of values while assigning the indexes visited the size of the set

n = int(input())
arr = list(map(int, input().split()))
g = {}

for i in range(len(arr)):
    x = arr[i] + i
    if x >= 0 and x < len(arr):
        g[x] = g.setdefault(x, set()) | {i}
memo = {}

def findEnd(s):
    visited = set()
    while True:
        if s in visited:
            cycle = set()
            res = []
            while s not in cycle:
                cycle.add(s)
                res.append(s)
                s += (arr[s] if arr[s] >= 0 else -abs(arr[s]))
            return res
        visited.add(s)
        x = (arr[s] if arr[s] >= 0 else -abs(arr[s]))
        if s + x < 0 or s + x >= len(arr):
            return [s]
        s += x

def dfs(stack, memo):
    cycle = set() if len(stack) == 1 else set(stack)
    stack = [stack]
    v_count = {x:1 for x in cycle}
    # need to deal with cycles
    # need to deal with keeping track of v_count, thinking of using dict and adding +1 per occurance.

    while len(stack) > 0:
        # problem area
        if len(stack[-1]) == 0:
            stack.pop()
            if len(stack) != 0:
                x = stack[-1].pop()
                v_count[arr[x]] -= 1
                if v_count[arr[x]] == 0:
                    del v_count[arr[x]]
            continue

        s = stack[-1][-1]
        v_count[arr[s]] = v_count.setdefault(arr[s], 0) + 1

        if s in g:
            next_row = []
            for next_s in g[s]:
                if next_s not in cycle:
                    next_row.append(next_s)
            stack.append(next_row)

        memo[s] = len(v_count.keys())
 
res = 0 
for s in range(len(arr)):
    if s not in memo:
        stack = findEnd(s)
        dfs(stack, memo)
    res += memo[s]
print(res)