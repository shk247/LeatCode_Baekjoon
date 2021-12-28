from typing import NamedTuple, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = None 
        curr = head 
        
        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
            
        return prev
        
    def reverse(self, current, prev):
        if not current:
            return prev
        
        next = current.next
        current.next = prev
        return self.reverse(next, current)
                    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
        
    
if __name__=='__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    
    Solution().reverseList(node)