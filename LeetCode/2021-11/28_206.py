from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return p 

if __name__ == '__main__':
    sol = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    print(sol.reverseList(node))