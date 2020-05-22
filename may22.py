class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        front = None
        output = ''
        for idx, i in enumerate(self.countAndSay(n-1)):
            if i != front:
                if front != None:
                    output = output + str(count) + front
                elif idx == 0 and n == 2:
                        output = output + str(1) + i        
                front = i
                count = 1
            else:
                count += 1
        
        if n > 2:
            output = output + str(count) + i
        return output