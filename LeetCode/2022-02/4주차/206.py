from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(-1)
        answer = root
        
        while head:
            tmp = root
            root = head.next 
            root.next = tmp 
            
            head = head.next
            root = root.next
            
        return answer.next
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr 
            curr = nextNode
            
        return prev

        