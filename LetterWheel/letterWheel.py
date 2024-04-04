import sys
import math
debug = True
test_num = 3

    # the idea here is to shrink the array combinations down to only the potentially valid sets
    # then perform a check to make sure all items are aligned on the valid sets
    # return the check that requires the smallest increment total

def get_combinations(n):
    res = []
    def helper(n, curr_arr = [], visited = set()):
        if len(curr_arr) == n:
            res.append(curr_arr.copy())
        for i in range(n):
            if i not in visited:
                curr_arr.append(i)
                visited.add(i)
                helper(n, curr_arr, visited)
                visited.remove(i)
                curr_arr.pop()
    helper(n)
    return res

def get_permutations(a, b):
    res = []
    for x in (1, -1):
        for y in (1, -1):
            res.append((a*x, b*y))
    return res

def is_valid3(lw, a1, a2):
    n = len(lw)
    flag = True
    for i in range(n): 
        test_set = set()
        test_set.add(lw[i][x])
        test_set.add(lw[(i + a1x + n) % n][y])
        test_set.add(lw[(i + a2x + n) % n][z])
        if len(test_set) != 3:
            flag = False
    if flag == True:
        return True
    return False
def get_valid2(lw):
    n = len(lw)
    valid = []

    # finds all the valid shifts of level a against level b
    def find_valid(a, b):
        valid = set()
        for i in range(n):
            flag = True
            for j in range(n):
                if lw[(i+j)%n][a] == lw[j][b]:
                    flag = False
                    break
            if flag == True:
                x = i - n if i > math.floor(n/2) else i
                valid.add(x)
        return valid
    
    # the idea here is to shrink the array combinations down to only the potentially valid sets
    # then perform a check to make sure all items are aligned on the valid sets
    # return the check that requires the smallest increment total

    # might need to check if top valid against mid, then top and mid against bot.
    # I think comparison can be figured out by adding adding items against each other, also maybe
    #   the numbers being added to each other should be within the -half to half range

    # after I find valid sets, the next step would be to minimize checked distances.

    valid.append(find_valid(0, 1))
    valid.append(find_valid(0, 2))

    valid.append(find_valid(1, 0))
    valid.append(find_valid(1, 2))

    valid.append(find_valid(2, 0))
    valid.append(find_valid(2, 1))
    
    return valid




def get_letter_wheel():
    top = [c for c in input()]
    mid = [c for c in input()]
    bottom = [c for c in input()]

    letter_w = list(zip(top, mid, bottom))
    return letter_w

def find_min_adjust(lw, valid):
    n = len(lw)
    res = -1
    for i in range(math.ceil(n / 2)):
        adj1 = i
        for j in range(0, i+1):
            adj2 = j

            # is valid
            
    return res

if debug == True:
    for i in range(1, test_num+1):
        sys.stdin = open(f"LetterWheel/letterwheels/{i}.in", "r")
        lw = get_letter_wheel()
        # print(lw)
        v = get_valid2(lw)
        for v1 in v:
            print(v1)
        print()
        # print(find_min_adjust(lw))
else:
    lw = get_letter_wheel()
    print(find_min_adjust(lw))

