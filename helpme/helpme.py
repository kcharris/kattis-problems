import sys
sys.stdin = open("helpme\input.txt") # comment this section to read from keyboard

def getAscii(row):
    return chr(row + ord('a'))
column_strings = []
# the index of a possible value letter is 4 * 8 + 1
for i in range(17):
    col = input()
    if i % 2 == 1:
        column_strings.append(col)
        
w_pieces = {'k':[], 'q':[], 'r':[],'b':[], 'n':[], 'p':[]}
b_pieces = {'K':[], 'Q':[], 'R':[],'B':[], 'N':[], 'P':[]}

for i in range(len(column_strings)):
    w_col_str = column_strings[i]
    b_col_str = column_strings[7-i]
    for j in range(2, len(w_col_str), 4):
        if w_col_str[j] in w_pieces:
            w_pieces[w_col_str[j]].append(getAscii(j//4) + str(7 - i + 1))
        if b_col_str[j] in b_pieces:
            b_pieces[b_col_str[j]].append(getAscii(j//4) + str(i + 1))

w_output = []
b_output = []

if len(w_pieces['k']): w_output.append(",".join(["K" + x for x in w_pieces['k']]))
if len(w_pieces['q']): w_output.append(",".join(["Q" + x for x in w_pieces['q']]))
if len(w_pieces['r']): w_output.append(",".join(["R" + x for x in w_pieces['r']]))

if len(w_pieces['b']): w_output.append(",".join(["B" + x for x in w_pieces['b']]))
if len(w_pieces['n']): w_output.append(",".join(["N" + x for x in w_pieces['n']]))
if len(w_pieces['p']): w_output.append(",".join([x for x in w_pieces['p']]))


if len(b_pieces['K']): b_output.append(",".join(["K" + x for x in b_pieces['K']]))
if len(b_pieces['Q']): b_output.append(",".join(["Q" + x for x in b_pieces['Q']]))
if len(b_pieces['R']): b_output.append(",".join(["R" + x for x in b_pieces['R']]))

if len(b_pieces['B']): b_output.append(",".join(["B" + x for x in b_pieces['B']]))
if len(b_pieces['N']): b_output.append(",".join(["N" + x for x in b_pieces['N']]))
if len(b_pieces['P']): b_output.append(",".join([x for x in b_pieces['P']]))

w_expected_res = "White: Ke1,Qd1,Ra1,Rh1,Bc1,Bf1,Nb1,a2,c2,d2,f2,g2,h2,a3,e4"
b_expected_res = "Black: Ke8,Qd8,Ra8,Rh8,Bc8,Ng8,Nc6,a7,b7,c7,d7,e7,f7,h7,h6"

b_res = "Black: " + ",".join(w_output)
w_res = "White: " + ",".join(b_output)

print(w_res)
print(b_res)