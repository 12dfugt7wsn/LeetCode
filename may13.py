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