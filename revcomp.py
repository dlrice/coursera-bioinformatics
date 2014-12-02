#!/usr/bin/env python

def main():
    text = open("dataset_3_2.txt").read().strip()
    rc = reverse_complement(text)
    f = open('rc.txt', 'w')
    f.write(rc)
    f.close()

def reverse_complement(p):
    
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    return ''.join([complement[p[i]] for i in range(len(p) - 1, -1, -1)])  

if __name__ == "__main__":
    main()
