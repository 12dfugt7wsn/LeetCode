class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def BinarySearch(l, h, nums, val):
            mid = int((l + h) / 2)
            if l>h:
                return l
            elif nums[mid] == val:
                return mid
            elif nums[mid] > val:
                return BinarySearch(l, mid-1, nums, val)
            else:
                return BinarySearch(mid+1, h, nums, val)

        return BinarySearch(0,len(nums)-1,nums,target)



class NewSolution:
	def isValidSudoku(self, board: [[str]]) -> bool:
		row = [set() for _ in range(9)]
		col = [set() for _ in range(9)]
		box = [set() for _ in range(9)]
		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if num == '.':
					continue

				if num in row[i] or num in col[j] or num in box[(i//3)*3 + j//3]:
					return False

				row[i].add(num)
				col[j].add(num)
				box[i//3*3+j//3].add(num)

		return True

