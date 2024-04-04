import sys
sys.stdin = open("sequences\sequences\1.in", "r")

# this would be how to turn the binary into a number the problem is that some indexes are '?'
num = int("0b" + input())

# keep a memo of the end of the binary number I'm currently checking
memo = {}

# The input string has up to 500,000 characters........
# while reading from right to leftt
# I will run into ones, and at any given point there will be a potential number of ones before this one
# that potential is defined by question marks and defined indexes.
# for the number ?10?0.
# index -1 is 0
# index -2 is either (number of zero's) + res, or 0
# index -3 is 0
# indexx -4 is number of (possible zeros * number of possible ones) + res