#complementary strands
import argparse
import os
#cmd line parser
parser = argparse.ArgumentParser(description='Enter input strings')
parser.add_argument('-s', type=str)
args = parser.parse_args()
s = args.s
out = ""
for letter in s:
    if letter == "A":
        out += "T"
    if letter == "C":
        out += "G"
    if letter == "G":
        out += "C"
    if letter == "T":
        out += "A"
i = len(out) - 1
res = ""
while i >= 0:
    #print(out[i], end = '')
    res+=(out[i])
    i -= 1

print(res)