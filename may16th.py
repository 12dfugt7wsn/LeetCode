def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    ref,start,prev = head,head,head
    for i in range(n):
        ref = ref.next
    if ref == None:
        head = head.next
    while(ref!=None):
        prev = start
        start = start.next
        ref = ref.next
    prev.next = start.next
    return head

def isValid(self, s: str) -> bool:
        while True:
            prev = len(s)
            for par in ['()','[]','{}']:
                s = s.replace(par, '')
            curr = len(s)
            
            if curr == prev:
                break
        
        return len(s) == 0

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
        while(True):
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                smallerval = 0
                if l1.val < l2.val:
                    smallerval = l1.val
                    l1 = l1.next
                else:
                    smallerval = l2.val
                    l2 = l2.next
                newNode = ListNode(smallerval)
                ptr.next = newNode
                ptr = ptr.next
        return head.next