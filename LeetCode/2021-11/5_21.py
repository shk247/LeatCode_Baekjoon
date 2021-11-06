from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.next <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
        
        prev.next = l1 if l1 else l2 

        return prehead.next

def All(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

if __name__ == '__main__':
    sol = Solution()
    n1 = ListNode(1, ListNode(2, ListNode(4)))
    n2 = ListNode(1, ListNode(3, ListNode(4)))   
    print(All(sol.mergeTwoLists(n1, n2)))