from collections import Counter, defaultdict

def main():
    dna = open("E-coli.txt").read()
    print count_kmers_v2(s=dna, k=9, t=3, L=500)

def count_kmers_v2(s, k, t, L):

    c = defaultdict(int)
    kmers_pass = set()
    
    for i in range(L - k + 1):
        kmer = s[i:i + k]
        c[kmer] += 1
        if c[kmer] == t:
            kmers_pass.add(kmer)
            
    for i in range(1,len(s) - L + 1):
        
        old = s[i - 1:i + k - 1]
        c[old] -= 1
        new = s[i + L - k:i + L]
        c[new] += 1
        if c[new] == t:
            kmers_pass.add(new)
    
    return len(kmers_pass)


def count_kmers(s, k, t, L):

    window = s[:L]
    kmers = [window[i : i + k] for i in range(0, L, k)]
    c = Counter(kmers)
    kmers_pass = set()
    
    for kmer, count in c.most_common():
        if count >= t:
            kmers_pass.add(kmer)
        else:
            break
                
    for i in range(1,len(s) - L):
        
        old = s[i - 1:i + k - 1]
        c[old] -= 1
        new = s[i + L - k + 1:i + L + 1 ]
        c[new] += 1
        if c[new] >= t:
            kmers_pass.add(new)
    
    return len(kmers_pass)

if __name__ == "__main__":
    main()