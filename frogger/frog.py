# import sys
# sys.stdin = open("frogger/1dfroggerhard/sample1.in", "r")

# ran into a large issue, I'm searching for a magic number and could end up at this number multiple times in a
# sinlge path. I only need to record or find the one that is closest to any given point. I should be able to handle
# this by saying that any duplicate values that I run into are invalid, but I need a way to track this.

# it's count could be the len of the set of vals I run into starting from the bottom.

# next idea to try would be to use s to store the number of values that s can reach including itself
# small issue with dealing with cycle, every item of the cycle should contain the cycle value.
# maybe start with recursion and convert to iteration
n = int(input())
arr = list(map(int, input().split()))

memo = {}
def frog(s, memo, visited):
    # out of bounds gets 0
    if s < 0 or s >= len(arr):
        return set()
    # the value has been computed before if s is set in memo
    if s in memo:
        return memo[s]
    # if found without a value, but has been seen then it is part of a cycle
    if s in visited:
        # record the indexes in the cycle, and assign them the value of them being able to
        # reach every node in the cycle including itself, which is len(cycle)
        curr_cycle = set()
        while s not in curr_cycle:
            curr_cycle.add(s)
            s += arr[s] if arr[s] >= 0 else -abs(arr[s])
        v = set()
        for x in curr_cycle:
            v.add(arr[x])
        memo[s] = v
        # because I exit the while loop after finding the first entry again. S will stay the same.
        return memo[s]
    
    visited.add(s)
    next_s = s + (arr[s] if arr[s] >= 0 else -abs(arr[s]))

    # deeper levels can set s, need to make sure nothing is over written here
    res = {arr[s]} | frog(next_s, memo, visited)
    if s not in memo:
        memo[s] = res
    return memo[s]
    
res = 0 
for s in range(len(arr)):
    res += len(frog(s, memo, visited = set()))
print(res)