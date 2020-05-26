class Solution:
    def jump(self, nums: [int]) -> int:
        minimum_jump_index = 0 #index value where we can jump through
        res=[0]*len(nums) # maintain record of jumps at a particular index
        i = 1
        while(i<len(nums) and i > minimum_jump_index):
            if minimum_jump_index + nums[minimum_jump_index]>=i:
                res[i]=res[minimum_jump_index]+1 #increment the value of that index from where minimum_jump_index has to jump
                i+=1 #increment the index till maximum_jump_index can jump through or say farthest position of jump
                
            else:
                minimum_jump_index+=1 # if it crosses the farthest jump, then increment the minimum_jump_index
                
        if res[-1]==0: # if last index indicates 0, it means no jump would be possible to reach at last index
            return 0

        else:
            return (res[-1]) # otherwise, print the last value which indicates how many jumps would get there to reach at last index


class secSolution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        
        def recPermute(res,lis,rem):
            if len(rem) == 0 :
                res.append(lis)
                return
            for i,val in enumerate(rem):
                recPermute(res, lis + [val] ,rem[:i] + rem[i+1:])

        for i in range(len(nums)):       
            recPermute(res,[nums[i]],nums[:i] + nums[i+1:])   
        return res

from collections import Counter

class thirdSolution:
    def permuteUnique(self, nums: [int]) ->[[int]]:
        counter = Counter(nums)
        def dfs(permutation, res):
            if not counter:
                res.append(permutation)
                return
            for key in set(counter.keys()):
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
                dfs(permutation + [key], res)
                counter[key] += 1
        res = []
        dfs([], res)
        return res