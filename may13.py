def romanToInt( s: str) -> int:
    symbol = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
    value = [1,5,10,50,100,500,1000,4,9,40,90,400,900]
    
    if len(s) == 0:
        return 0
    result = 0 
    i = 0 
    while i in range(0,len(s)):
        print('i',i)
        if (s[i] in ['I','X','C'])and (i < len(s)-1) and (s[i:i+2] in symbol):
                result += value[symbol.index(s[i:i+2])]
                i += 1
                print(result,i)       
                
        else:
            result += value[symbol.index(s[i])]
        i += 1
    return result 

print(romanToInt("MCMXCIV"))

def longestCommonPrefix(self, strs: [str]) -> str:
    res, i, j = '', 0, 0
    try:
        while True:
            if i == len(strs) - 1:
                res += strs[0][j]
                i = 0
                j += 1
            if strs[i][j] == strs[i+1][j]:
                i += 1
            else:
                return res
    except:
        return res

def threesum(self, nums: [int]):
    result = set()
    mapping = {}
    geq0 = set()
    leq0 = set()
    for i in nums:
        mapping[i] = 1 if i not in mapping.keys() else mapping[i] + 1
        if i >= 0:
            geq0.add(i)
        if i <= 0:
            leq0.add(i)
    
    for a in geq0:
        for b in leq0:
            c = - a - b
            potential = [a, b, c]
            if c in mapping.keys() and mapping[c] >= sum([x == c for x in potential]):
                result.add(tuple(sorted(potential)))
    return result