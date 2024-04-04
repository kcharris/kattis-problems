import sys
sys.stdin = open("frogger/1dfroggerhard/sample1.in", "r")

# travel down lines that have not been gone down yet, find out if it leads to a cycle or an end
# then do a dfs with a building set of values while assigning the indexes visited the size of the set
n = int(input())
arr = list(map(int, input().split()))
g = {}
memo = {}

for i in range(len(arr)):
    x = arr[i] + i
    if x >= 0 and x < len(arr):
        g[x] = g.setdefault(x, set()) | {i}

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

def dfs(idx_arr, memo):
    # perform the first calculation in a topological sort
    counter = {}
    stack = []
    next_layer = []
    idx_arr = set(idx_arr)
    for i in idx_arr:
        counter[arr[i]] = counter.setdefault(arr[i], 0) + 1
    for i in idx_arr:
        memo[i] = len(counter)
        if i in g:
            for j in g[i]:
                if j not in idx_arr:
                    next_layer.append(j)
    stack.append(next_layer)

    # now perform topological sort using stack, layers need to be kept track of.
    while len(stack) > 0:
        # make sure layer contains value else pop and continue
        # a value must be reduced or removed when an empty array is popped, this value will be the one that created array
        if len(stack[-1]) == 0:
            stack.pop()
            if len(stack) > 0 and len(stack[-1]) > 0:
                val = arr[stack[-1].pop()]
                counter[val] -= 1
                if counter[val] <= 0:
                    del counter[val]
            continue

        curr_i = stack[-1][-1]
        counter[arr[curr_i]] = counter.setdefault(arr[curr_i], 0) + 1
        
        memo[curr_i] = len(counter)

        next_arr = []
        if curr_i in g:
            for i in g[curr_i]:
                next_arr.append(i)
        stack.append(next_arr)

res = 0 
for s in range(len(arr)):
    if s not in memo:
        stack = findEnd(s)
        dfs(stack, memo)
    res += memo[s]
print(res)