from typing import Optional

def mysolution(l1, l2):
    if not l1 and not l2:
        return []
    elif not l1 or not l2:
        return l2 if not l1 else l1
    else:
        total = [list(i) for i in list(zip(l1,l2))]
        return sum(total,[])

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

if __name__ == '__main__':
    print()