#DNA to RNA
import argparse
import os
#cmd line parser
parser = argparse.ArgumentParser(description='Enter input strings')
parser.add_argument('-s', type=str)
args = parser.parse_args()
s = args.s
out = ""
for letter in s:
    if letter == 'T':
        out += 'U'
    else:
        out += letter
print(out)