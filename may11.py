def reverse(x: int) -> int:
    if x >= 2**31-1 or x <= -2**31: return 0
    
    if x >= 0 :
        temp = str(x)
        temp = temp[::-1]
    else:
        x = -x 
        temp = str(x)
        temp = temp[::-1]
        temp = '-' + temp
    if int(temp) >= 2**31-1 or int(temp) <= -2**31: return 0
    else: return int(temp)

def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0 
        i = 0 
        while i < len(str) and str[i] ==' ':
            i += 1
        str_new = str[i:]
        if len(str_new) == 0:
            return 0
        
        first = str_new[0] 
        if first not in '0123456789+-':
            return 0 
        else:
            x = ''
            j = 0 
            while  j < len(str_new) and ((str_new[j] in '0123456789') or (j == 0 and (first== '+' or first=='-' ))):

                x += str_new[j]
                j += 1
            if x == '+' or x == '-':
                return 0
            x = int(x)

            if x >= 2**31-1 : return 2147483647
            elif x <= -2**31: return -2147483648
            else: return x

def isPalindrome(self, x: int) -> bool:
        return (str(x) == str(x)[::-1])
