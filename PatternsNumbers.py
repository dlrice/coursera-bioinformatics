
NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
SymbolToNumber = {'A':0, 'C':1, 'G':2, 'T':3}

def NumberToPattern2(n, k):
    pattern = [NumberToSymbol[0] for el in range(k)]
    for i in range(k - 1, -1, -1):
        pattern[i]= NumberToSymbol[n % 4]
        n /= 4
    return ''.join(pattern)
    
def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol[index]
    prefixIndex = index / 4
    r = index % 4
    prefixPattern = NumberToPattern(prefixIndex, k - 1)
    return prefixPattern + NumberToSymbol[r]

def PatternToNumber(pattern):
    if len(pattern)  == 0:
        return 0
    return 4 * PatternToNumber(pattern[:-1]) + SymbolToNumber[pattern[-1]]

if __name__ == "__main__":
    NumberToPattern2(732723242334323249, 20)
    import timeit
    print(timeit.timeit("NumberToPattern2(732723242334323242342343892378972348989238923233, 100)", setup="from __main__ import NumberToPattern2"))
    #print PatternToNumber('GATACAGGGAATAACA')
