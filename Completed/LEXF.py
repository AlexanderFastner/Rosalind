#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n(n≤10).
#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
#python LEXF.py -n 10 -s A B C D E F G H I J
#python LEXF.py -n 2 -s A B C D
#---------------------------------------------------------------------------------------------------
import argparse
import itertools
#---------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='Enter a positive integer, and up to 10 symbols')
parser.add_argument('-n', type=int)
parser.add_argument('-s', nargs='+', type=str)
args = parser.parse_args()
n = args.n
s = args.s
print("n: ",n)
#---------------------------------------------------------------------------------------------------
#ensure correct ordering of s
s = sorted(s)
s = ''.join(s)
print("s: ", s)
#---------------------------------------------------------------------------------------------------
def s_generator(alphabet, length):
    for s in itertools.product(alphabet, repeat=length):
        yield ''.join(s)

# Example usage
result = list(s_generator(s, n))
for r in result:
    print(r)
#---------------------------------------------------------------------------------------------------