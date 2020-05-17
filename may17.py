def generateParenthesis( n: int) -> [str]:
        res = []
        dfs(res, n, n, '')
        return res

    
def dfs( res, left, right, path):
    if left == 0 and right == 0:
        print('path',path)
        res.append(path)
        return
    
    if left > 0:
        dfs(res, left - 1, right, path + '(')
        
    if left < right:
        dfs(res, left, right - 1, path + ')')

print(generateParenthesis(2))

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return 
        result=[]
        for i in lists:
            while i:
                result.append(i.val)
                i=i.next
        if not result: return
        result.sort()
        head=ListNode(result.pop(0))
        m=head
        while result:
            m.next=ListNode(result.pop(0))
            m=m.next
        return head

def swapPairs(self, head: ListNode) -> ListNode:
        if not head:return
        prev,nxt=head,head.next
        while nxt:
            prev.val,nxt.val=nxt.val,prev.val
            if nxt.next:
                prev=prev.next.next
                nxt=nxt.next.next
            else:break
        return head