#count A C G T 
s = "TAGCAGCGATGACAGCGCAATCGAGTGTTGTCTTTAACTAGAGACAGAGGAGTAAATCTTGATTCGACGCTGCTATCAAGCCATCAGAGTTTGAGAGGTTTAAAGAAGTGAGCGACAAGGCAATGGATGACCTAGCGAGCACAATGCGCACGCCTTAAGGCGGGGGAACAGTGAGCTCAACTACAACTCCGGTCTTATAAGTTATGAGGATCTTCCGCCCTCATCCATACGCAGACCAGAATCTGACAGTTACAGGGGTGGTTCATTCTGCCAAACCTCTAAAGGTCACGTATCTGCATACGCTAATGTACTGCTGTAGTCTGATCGTCAATCGTGTAAGCATAGCGGCGCGGACTAGATAGTATACAACGTGACCAACTGACCACGCAGACAGCGTTTAGCTGAAATCAGCCCATAGACCTTATCTCGCAGTCCGTTACTGACAAGACGAACTGTGAGGTCTCCCTAAGATTTGCTCTATAACATGCCGGGGGCCATCTCGGCTACCAGGATTGCAATCGTGGGGAATGACGCTTCTATTCAAGCGTGCGGTGTCCGGCATTTTTAAATAACCGGACTAATACTATCCAGGGTGGACCATGAATAACGGCAAATCCACGGGGGTAACGGACCGGGTAGCTCCCCGTTTGATTTGGACAAGCACTGCTAGTAACAGAATTACTGGTTTAATGTACGAGTAACACATTGGCGAAGATTAACTTGACCGAAGAGCCAGATGTGTGCGAACACTGTGTACTGGCTGTATCCATGGAATTCTGAGGCCGGCCATTGTTATGACTTACAAGTTGCTTGGCTCTATTCAATACTACACAACTGGTGACGATTTCCATAGGGTTAGACACATACGTACGCGCGTCATTACGTCCGGGCCAGTACGAGACAATTGGGTGATCAACCCA"
A = 0
C = 0 
G = 0
T = 0
for letter in s:
    if letter == 'A':
        A +=1
    if letter == 'C':
        C +=1
    if letter == 'G':
        G +=1
    if letter == 'T':
        T +=1
print(A, C, G, T)