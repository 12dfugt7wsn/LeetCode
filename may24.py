import collections
class Solution:
    def __init__(self):
        self.answer=set()   # Set - To get rid of duplicates
        self.candidates=[]  

    def helper(self,target_,ans_=[]):
        if target_ < 0 : return
        elif target_ == 0 : 
            self.answer.add(tuple(sorted(ans_))) # Sets can store only tuples not lists 
            return          # Sorting it to make it distinguishable
        else:
            for i in self.candidates:
                self.helper(target_-i,ans_+[i])

    def combinationSum(self, candidates, target) -> [[int]]:
        self.candidates = candidates # Making it a data member caus' it never changes and 
        self.helper(target)          # no need to pass it for every recursion call
        return list(self.answer)

class secSolution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if not nums:
            return 1
        
        maxs = max(nums)
        
        if maxs <= 0:
            return 1
        
        for i in range(1, maxs+1):
            if not i in nums:
                return i
        return maxs+1


class thirdSolution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        dp = collections.defaultdict(set)
        candidates.sort()
        dp[0].add(())
        for n in candidates:
            for i in reversed(range(n, target + 1)):
                if i >= n:
                    for seq in dp[i-n]:
                        dp[i].add(seq+(n,))
        return dp[target]