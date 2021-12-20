from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]
    
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        deq = deque()
        
        node = head
        while node:
            deq.append(node.val)
            node = node.next
        
        while deq:
            if deq.pop() != deq.popleft():
                return False
        return True
    
    def isPalindrome3(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        rev = None
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        
        return not rev
        
        
        

if __name__=='__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(1)
    
    Solution().isPalindrome(node)