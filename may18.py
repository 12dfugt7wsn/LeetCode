# def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #if the list is empty
        # if not head:
        #     return
        # #finding total length of list
        # cur = head
        # length = 0
        
        # while cur:
        #     length += 1
        #     cur = cur.next
            
        # # returning head if k is greater than total length of the list
        # if k > length :
        #     return head
        
        # #reversing the first k nodes seperately and assigning head
        # prev = None
        # cur = head
        # count = 1
        # while cur and count <= k:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        #     count += 1
        # temp1 = head # temporary variable to assign prev of next reversing
        # head.next = cur
        # head = prev
        # prev = temp1
        
        # # reversing next subsequent k nodes 
        # limit = k+k # to keep track of reversing within length of the list
        # while limit <= length:
        #     dummy_prev = prev
        #     dummy_cur = cur
        #     count = 1
        #     while cur and count <= k:
        #         temp = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = temp
        #         count += 1
        #     dummy_prev.next = prev
        #     dummy_cur.next = cur
        #     prev = dummy_cur
        #     limit += k
        
        # return head


def removeDuplicates(self, nums: [int]) -> int:
    l, r = 0, 1
    while r < len(nums):
        while r < len(nums) and nums[l] == nums[r]: r += 1
        if r < len(nums):
            nums[l+1] = nums[r]
            l += 1; r += 1
    return l+1

def removeElement(self, nums: [int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
        return(len(nums))