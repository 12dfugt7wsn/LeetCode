def rotate( a: [[int]]) -> None:
    for r in range( (len(a)+1) // 2 ):
        for c in range( len(a) // 2 ):
            temp = a[r][c]
            # four rotations to go all the way around
            for _ in range(4):
                # a rotation is equivalent to:
                # "flip the row, then swap the row and col"
                c, r = len(a)-1-r, c
                # current location gets val from prev rotation
                # next location gets this val
                temp, a[r][c] = a[r][c], temp

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        groups = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        return groups.values()

class newSolution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            if n % 2 == 1:
                return x * tmp * tmp

        if n >= 0:
            return helper(x, n)

        return 1 / helper(x, -n)