#Given: A DNA string of length at most 1 kbp in FASTA format.
#The position and length of every reverse palindrome in the string having length between 4 and 12. 
#You may return these pairs in any order.

#code to find reverse palindromes.

#for each window size 4-12:
    #starting at i, going through s:
        #if i-i+window size is a palindrome:
            #add i + " " + window size to out

#for entry in out:
    #print(entry)


s = "ATATTGCGTTGGCCCATTGAAATTATCTATAGCTCGGGTAGGAGTCCTATAGAATCACAAAGCGTAGGTACTACTTTAATCGTCCATGCATTAGAATTATAACTGGACGTCACCTCTCAAAGGGGTGAATATCGTTTAGCAAGAACCATCAGTATGGGTTGGGACTTCTCAGGTTAGAACACTGGAGGTATGGGTCGCCTGAAAAGGTTACCAGATATCCGGCTGTTAACCTATTTCGCCTTTTCAAGGGCAGACCGAATGCTCCTTGACGAAGGAGGCCATTCGGGGTGCACTCTCGTGCCTTCATTCTAGTGGCTTCGCAATGGTGGTCTCGTAGGGGGTAGATATACCTAGTAGCTAACCCATACAACGCTAGTGGCCACCCGCCACGAGCTTCGAGGCTCTAAGACACCTCCTCAAAGCTAGCATAATAGCGGCAAACCTCGTCCCGAATCTGCGGATCAGCCGACGATGCGCGAATTCGGATCTTTCGAAAGATGGGCACACCGGAACCGGTATGACGTCTTAAACCTGGTGGCCTACTGTGTGGATTAAGTCCTATTCTCACGAAAAGGGTTTCACCCGTGCTCTGGATCGACAGCCGGTAGTCGGAAGGAGTGCTTCTCGTTATCATGGCGCTAAGCCAGACCGAACGCTAAAATAAGTCTCCGGCTCACAAGAATAGATAACGTAGCCATAGTCTGATCAGGCAACCTGCCTTTGTTTCGCCGTTGTCTTTATATATTAACGGGACTGTATACATCATATATCATGATCGGCTAGGGAAGTGTGCTTTGGTTGCGAACTGTTGGATCCGACTAGTCCGAAAGTATCGGGATGCGTTCTAAATTTTAATCTGACAGGTGGCGTTCAGAAGGAGCGTGGGCAGATTTTCTGCCTGGCACCGGCAGGGAAAAGGTAAGACGTATGCAAGACTTCGAGGAGCTGCAGTAGGAGATGCCATTGCGTATAGAACATAACGCG"
out = []

def reverseComplement(sub):
    new = ""
    for letter in sub:
        if letter == "A":
            new += "T"
        if letter == "C":
            new += "G"
        if letter == "G":
            new += "C"
        if letter == "T":
            new += "A"
    i = len(new) - 1
    res = ""
    while i >= 0:
        res+=(new[i])
        i -= 1
    return res

def isPalindrome(sub):
    if reverseComplement(sub) == (sub):
        return True
    else:
        return False

w = 4
while w < 13:
    index = 0
    while index < len(s) + 1 - w:
        sub = s[index:(index + w)]
        if isPalindrome(sub):
            b = [(index + 1), w]
            out.append(b)
        index += 1
    w += 1

#print(out)
out = sorted(out, key = lambda x : x[0], reverse = False)
#print(out)

#no newline at the end
with open("REVPout.txt", "w") as o:
    for entry in out:
        for i,e in enumerate(entry):
            if i == 0:
                o.write(str(e) + " ")
            else:
                o.write(str(e))
        o.write(" ")
