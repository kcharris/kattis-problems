debug = False
tests = [i + 1 for i in range(3)]
# problem may be able to be solved using variant of longest common substring
from pprint import pprint
import sys

faces = {"A", "K", "Q", "J", "T"}
suits = {"H", "D", "C", "S"}
d = {"total": 0, "A":0, "K":0, "Q":0, "J":0, "T":0, "H":0, "C":0, "D":0, "S":0, "KS":0}
for i in range(2,10):
    d[str(i)] = 0

def getPrefixDict(arr):
    d_prefix = [d.copy() for _ in range(len(arr) + 1)]

    # create and update 2 prefix arrays, one containing values, and the other containing dictionaries of seen cards
    for i in range(len(arr)):
        card = arr[i]
        # hard to filter over KS, but I could just ignore sets that have more than 0 KS.
        if card == "KS":
            d_prefix[i+1][card] += 1

        for k in d:
            d_prefix[i+1][k] += d_prefix[i][k]

        if card[0] in faces:
            if card[0] != "A":
                d_prefix[i+1]["total"] = d_prefix[i]["total"] + 10
            else:
                d_prefix[i+1]["total"] = d_prefix[i]["total"] + 1

        else:
            d_prefix[i+1]["total"] = d_prefix[i]["total"] + int(card[0])
        d_prefix[i+1][card[0]] += 1
        d_prefix[i+1][card[1]] += 1
    
    return d_prefix

# uses a sliding window to create a dictionary using values as keys, for each key contains an array of dictionaries where the card total is the value, and where there is not king of spades.
def getWindowDict(d_prefix, w_size):
    # perform a sliding window
    value_d = {}
    l = 0
    r = w_size
    while r < len(d_prefix):
        dict1 = d_prefix[r].copy()
        for k in dict1:
            dict1[k] -= d_prefix[l][k]
        if dict1["KS"] == 0:
            value_d[str(dict1.values())] = dict1["total"]

        l += 1
        r += 1
  
    return value_d

def findRes():
    n1, n2 = map(int, input().split())
    f_half = convert_to_lists(input().split())
    s_half = convert_to_lists(input().split())
    # print(f_half)
    # print(s_half)
    # print()

    res = 0
    f_value_d = {}
    s_value_d = {}
    for i in range(len(f_half)):
        f_li = f_half[i]
        f_prefix = getPrefixDict(f_li)
        w = min(100,len(f_li))
        while w > 0:
            f_value_d |= getWindowDict(f_prefix, w)
            w -= 1

    for j in range(len(s_half)):
        s_li = s_half[j]
        s_prefix =  getPrefixDict(s_li)
        w = min(100, len(s_li))
        
        while w > 0 and res // 2 <= w * 10:
            s_value_d |= getWindowDict(s_prefix, w)
            w -= 1
    for tup in f_value_d:
        if tup in s_value_d:
            res = max(res, f_value_d[tup]*2)
    print(res)

def test(test_nums):
    for t in test_nums:
        sys.stdin = open(f"input{t}.txt")
        findRes()
def convert_to_lists(li):
    new_list = []
    curr_li = []
    for i in range(len(li)):
        if li[i] == "KS" and len(curr_li) > 0:
            new_list.append(curr_li.copy())
            curr_li = []
        else:
            curr_li.append(li[i])
    if len(curr_li) > 0:
        new_list.append(curr_li.copy())
    return new_list

if debug:
    test(tests)
else:
    findRes()