class Solution:
    def trap(self, height: [int]) -> int:
        stack = []
        water = 0
        
        for i, e in enumerate(height):
            # we need to see if we can form a container
            while stack and e >= stack[-1][0]:
                popped, _ = stack.pop()
                # is it a container though? we have a left border?
                if stack: 
                    left_border, j = stack[-1]
                    # we compute the water
                    water += min(left_border-popped, e-popped)*(i-j-1)
            stack.append((e,i))
        return water


class newSolution:
    def multiply(self, num1: str, num2: str) -> str:
        first = 0
        second = 0
        for i in num1:
            current = ord(i) - ord('0')
            first = first*10 + current
        for i in num2:
            current = ord(i) - ord('0')
            second = second*10 + current
        return str(first*second)


class thirdSolution:
    def isMatch(self, s: str, p: str) -> bool:
        res = [False]*(len(s)+1)
        res[0] = True
        for cp in p:
            tres = [res[0] if cp=='*' else False]
            f = tres[0]
            for i, cs in enumerate(s):
                f |= res[i+1]
                if cp.isalpha():
                    tres.append(s[i]==cp and res[i])
                elif cp == '?':
                    tres.append(res[i])
                else:
                    tres.append(f)
            res = tres
        return res[-1]