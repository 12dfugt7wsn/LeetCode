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

class Solution:
    def getPosNums(self, board, position, rows, columns, sub_boxes):
        nums = []
        row, column = position
        box_idx = (row//3)*3 + column//3
        for s in map(str,range(1,10)):
            if (not s in rows[row]) and (not s in columns[column]) and (not s in sub_boxes[box_idx]):
                nums.append(s)
        return nums
    
    
    
    def init(self, board, emptyPos, rows, columns, sub_boxes):
        ## fill rows, columns, sub_boxes and emptyPos keys
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if tmp != '.':
                    rows[i].add(tmp)
                    columns[j].add(tmp)
                    box_idx = (i//3)*3+(j//3)
                    sub_boxes[box_idx].add(tmp)
                else:
                    emptyPos.append((i,j))
        return
        
        
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        emptyPos = []       # record empty position(row,column)
        rows = [set() for i in range(9)]    # record numbers in each rows
        columns = [set() for i in range(9)] # record numbers in each columns
        sub_boxes = [set() for i in range(9)]   #record numbers in each sub-boxes
        
        self.init(board, emptyPos, rows, columns, sub_boxes)
        

        def solve(board, positions):
            if not positions:       # if all empty positions are filled, it's done
                return True
            
            # we are working on first empty position
            # find all possible numbers on this position
            posNums = self.getPosNums(board, positions[0], rows, columns, sub_boxes)
            
            if not posNums:     #if there is no available numbers on this position, it's fail
                return False
            
            row, column = positions[0]
            box_idx = (row//3)*3 + (column//3)
            for s in posNums:
                board[row][column] = s
                rows[row].add(s)
                columns[column].add(s)
                sub_boxes[box_idx].add(s)
                
                if solve(board, positions[1:]):
                    return True
                
                rows[row].remove(s)
                columns[column].remove(s)
                sub_boxes[box_idx].remove(s)
                
            
            # if all possible numbers don't work, it's fail.            
            board[row][column] = '.'                    
            return False        
        
        solve(board, emptyPos)
        return

